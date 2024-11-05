import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_ASSISTANT_ID = os.getenv('OPENAI_ASSISTANT_ID')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL')
    YCLIENTS_API_URL = os.getenv('YCLIENTS_API_URL')
    YCLIENTS_PARTNER_TOKEN = os.getenv('YCLIENTS_PARTNER_TOKEN')
    YCLIENTS_USER_TOKEN = os.getenv('YCLIENTS_USER_TOKEN')
    YCLIENTS_COMPANY_ID = os.getenv('YCLIENTS_COMPANY_ID')


settings = Settings()
