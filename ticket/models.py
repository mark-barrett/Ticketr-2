from django.contrib.auth.models import User
from django.db import models

from event.models import Event


class Order(models.Model):
    order_number = models.CharField(max_length=20)
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    payment_amount = models.DecimalField(decimal_places=2, max_digits=6)
    status = models.BooleanField()

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name_plural = 'orders'


class OrderTicket(models.Model):
    # Value that generates the QR code
    ticket_number = models.CharField(max_length=20)
    order = models.ForeignKey(Order)
    event = models.ForeignKey(Event)
    used = models.BooleanField()

    def __str__(self):
        return self.ticket_number

    class Meta:
        verbose_name_plural = 'order Tickets'
