from aiogram import Dispatcher

from .common import register_common_handlers
from .registration import register_registration_handlers
from .menu import register_menu_handlers
from .services import register_services_handlers
from .booking import register_booking_handlers
from .contacts import register_contacts_handlers
from .prices import register_prices_handlers
from .faq import register_faq_handlers
from .unknown import register_unknown_handlers


def register_handlers(dp: Dispatcher):
    register_common_handlers(dp)
    register_registration_handlers(dp)
    register_menu_handlers(dp)
    register_services_handlers(dp)
    register_booking_handlers(dp)
    register_contacts_handlers(dp)
    register_prices_handlers(dp)
    register_faq_handlers(dp)
    register_unknown_handlers(dp)
