import markdown
from bs4 import BeautifulSoup, NavigableString
import re


def markdown_to_telegram_html(markdown_text: str) -> str:
    '''
    Преобразует переданный текст в формате Markdown в HTML, совместимый с Telegram.

    Args:
        markdown_text (str): Текст в формате Markdown для конвертации.

    Returns:
        str: Преобразованный текст в формате HTML, подходящий для использования в Telegram, с фильтрацией
        неподдерживаемых тегов и элементов.
    '''
    html_content = markdown.markdown(markdown_text, extensions=['extra', 'sane_lists'])

    def filter_supported_html(html):
        '''
        Фильтрует и модифицирует сгенерированный HTML, оставляя только теги, поддерживаемые Telegram.

        Args:
            html (str): Сгенерированный из Markdown HTML-контент.

        Returns:
            str: Отфильтрованный и изменённый HTML, совместимый с форматированием Telegram.
        '''
        soup = BeautifulSoup(html, 'html.parser')

        for tag in soup.find_all(['hr', 'ul']):
            previous = tag.previous_sibling
            while previous and isinstance(previous, NavigableString) and previous.strip() == '':
                to_remove = previous
                previous = previous.previous_sibling
                to_remove.extract()
            if tag.name == 'hr':
                tag.extract()
            elif tag.name == 'ul':
                for li in tag.find_all('li'):
                    li.insert_before(NavigableString('- '))
                tag.unwrap()

        for header_tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            header_text = ''.join(str(content) for content in header_tag.contents).strip()
            if header_text:
                bold_tag = soup.new_tag('b')
                italic_tag = soup.new_tag('i')
                for content in header_tag.contents:
                    italic_tag.append(content)
                bold_tag.append(italic_tag)
                header_tag.insert_before(NavigableString('\n\n'))
                header_tag.replace_with(bold_tag)
                # bold_tag.insert_after(NavigableString('\n'))

        for p in soup.find_all('p'):
            p.insert_before(NavigableString('\n'))
            p.insert_after(NavigableString('\n'))
            p.unwrap()

        for br in soup.find_all('br'):
            br.replace_with('\n')

        allowed_tags = {
            'b',
            'strong',
            'i',
            'em',
            'u',
            'ins',
            's',
            'strike',
            'del',
            'tg-spoiler',
            'a',
            'tg-emoji',
            'code',
            'pre',
            'blockquote',
            'blockquote_expandable',
        }
        for tag in soup.find_all(True):
            if tag.name not in allowed_tags:
                tag.unwrap()

        final_html = str(soup)

        final_html = re.sub(r'\n{3,}', '\n\n', final_html)
        final_html = final_html.strip()

        return final_html

    return filter_supported_html(html_content)
