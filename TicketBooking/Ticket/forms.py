from Ticket.models import Ticket
from django import forms

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['show', 'cinema', 'movie', 'quantity']
   
    
