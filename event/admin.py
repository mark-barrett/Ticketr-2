from django.contrib import admin

# Register your models here.
from event.models import *

admin.site.register(Organiser)
admin.site.register(Event)
admin.site.register(Ticket)