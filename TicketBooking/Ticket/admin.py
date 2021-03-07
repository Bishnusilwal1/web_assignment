from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Cast)
admin.site.register(Ticket)
admin.site.register(Show)
