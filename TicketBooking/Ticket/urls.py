
from django.urls import path

from .views import *

urlpatterns = [
    path('ticket_form/', tickets, name="ticket_form"),
    path('ticket_view/', ticket_lists, name="ticket_view"),
    path('cinemas/', cinemas, name="cinemas"),
    path('search_view/', search_query, name="search_view")
]