from config import settings
from yclients import YClientsManager


def get_manager():
    if not hasattr(settings, 'TELEGRAM_BOT_TOKEN') or not settings.TELEGRAM_BOT_TOKEN:
        raise ValueError('TELEGRAM_BOT_TOKEN is not set in settings.')

    if not hasattr(settings, 'YCLIENTS_API_URL') or not settings.YCLIENTS_API_URL:
        raise ValueError('YCLIENTS_API_URL is not set in settings.')

    if not hasattr(settings, 'YCLIENTS_PARTNER_TOKEN') or not settings.YCLIENTS_PARTNER_TOKEN:
        raise ValueError('YCLIENTS_PARTNER_TOKEN is not set in settings.')

    if not hasattr(settings, 'YCLIENTS_USER_TOKEN') or not settings.YCLIENTS_USER_TOKEN:
        raise ValueError('YCLIENTS_USER_TOKEN is not set in settings.')

    if not hasattr(settings, 'YCLIENTS_COMPANY_ID') or not settings.YCLIENTS_COMPANY_ID:
        raise ValueError('YCLIENTS_COMPANY_ID is not set in settings.')

    manager = YClientsManager(
        api_url=settings.YCLIENTS_API_URL,
        partner_token=settings.YCLIENTS_PARTNER_TOKEN,
        user_token=settings.YCLIENTS_USER_TOKEN,
        company_id=settings.YCLIENTS_COMPANY_ID,
    )
    return manager
