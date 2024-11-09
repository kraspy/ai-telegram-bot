import markdown
from bs4 import BeautifulSoup

SUPPORTED_TAGS = [
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
]


def markdown_to_telegram_html(markdown_text: str) -> str:
    '''Конвертирует Markdown в HTML, совместимый с Telegram.

    Args:
        markdown_text (str): Текст в формате Markdown.

    Returns:
        str: HTML-контент, совместимый с Telegram.
    '''
    html_content = markdown.markdown(markdown_text, extensions=['extra', 'sane_lists'])
    soup = BeautifulSoup(html_content, 'html.parser')

    for tag in soup.find_all(True):
        if tag.name not in SUPPORTED_TAGS:
            tag.unwrap()

    return str(soup)
