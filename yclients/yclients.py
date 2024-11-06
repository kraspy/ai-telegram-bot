from yclients.manager import YClientsManager

from yclients.services.clients_service.clients_service import ClientsService
from yclients.services.comments_service.comments_service import CommentsService
from yclients.services.journal_service import JournalService
from yclients.services.newsletter_service import NewsletterService
from yclients.services.online_bookings_service import OnlineBookingsService
from yclients.services.records_service import RecordsService
from yclients.services.services_service import ServicesService
from yclients.services.staff_schedule_service import StaffScheduleService
from yclients.services.user_records_service import UserRecordService
from yclients.services.validation_service import ValidationService
from yclients.services.visits_service import VisitsService


class YClients:
    def __init__(self, manager: YClientsManager):
        self.manager = manager

        self.clients = ClientsService(manager)
        self.comments = CommentsService(manager)
        self.journal = JournalService(manager)
        self.newsletter = NewsletterService(manager)
        self.online_bookings = OnlineBookingsService(manager)
        self.records = RecordsService(manager)
        self.services = ServicesService(manager)
        self.staff_schedule = StaffScheduleService(manager)
        self.user_records = UserRecordService(manager)
        self.validation = ValidationService(manager)
        self.visits = VisitsService(manager)

    async def close(self):
        '''Закрывает менеджер и связанные с ним ресурсы.'''
        await self.manager.close()
