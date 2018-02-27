from django.contrib import admin

# Register your models here.
from ticket.models import Order, OrderTicket

admin.site.register(Order)
admin.site.register(OrderTicket)