import markdown
from bs4 import BeautifulSoup


def markdown_to_telegram_html(markdown_text: str) -> str:
    html_content = markdown.markdown(markdown_text, extensions=['extra', 'sane_lists'])

    def filter_supported_html(html):
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all(True):  # Ищем все теги
            if tag.name not in [
                'b',  # жирный текст
                'strong',  # жирный текст (аналог <b>)
                'i',  # курсив
                'em',  # курсив (аналог <i>)
                'u',  # подчеркнутый текст
                'ins',  # подчеркнутый текст (аналог <u>)
                's',  # зачеркнутый текст
                'strike',  # зачеркнутый текст (устаревший, аналог <s>)
                'del',  # зачеркнутый текст (аналог <s>)
                'tg-spoiler',  # спойлер (Telegram)
                'a',  # ссылка
                'tg-emoji',  # emoji (Telegram)
                'code',  # встроенный код
                'pre',  # блок предформатированного кода
                'blockquote',  # блок цитирования
                'blockquote_expandable',  # блок цитирования с возможностью скрыть часть текста
            ]:
                tag.unwrap()
        return str(soup)

    return filter_supported_html(html_content)
