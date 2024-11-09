from aiogram.fsm.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    waiting_for_contact = State()
    waiting_for_fullname = State()


class BookingStates(StatesGroup):
    choosing_service = State()
    choosing_date = State()
    choosing_time = State()
    confirming = State()


class ServiceDescriptionStates(StatesGroup):
    choosing_service_description = State()


class FAQStates(StatesGroup):
    choosing_faq = State()
