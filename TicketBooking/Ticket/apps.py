from django.apps import AppConfig

class TicketConfig(AppConfig):
    name = 'Tickek'

    def ready(self):
        import Ticket.signalsa
