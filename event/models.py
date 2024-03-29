from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Organiser(models.Model):
    name = models.CharField(max_length=256)
    about = models.TextField(blank=True)
    image = models.ImageField(upload_to='static/organiser_images', blank=True, null=True)
    website = models.CharField(max_length=256, blank=True)
    facebook = models.CharField(max_length=256, blank=True)
    twitter = models.CharField(max_length=256, blank=True)
    background_colour = models.CharField(max_length=10, default='#D3D3D3', blank=True)
    text_color = models.CharField(max_length=10, default='#000000', blank=True)
    paypal_email = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Organisers'

    def __str__(self):
        return self.name


class Event(models.Model):

    title = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    image = models.ImageField(upload_to='static/event_images', blank=True, null=True)
    background_colour = models.CharField(max_length=7)
    description = models.TextField()
    organiser = models.ForeignKey(Organiser, on_delete=models.CASCADE)
    privacy = models.CharField(max_length=1)
    show_remaining_tickets = models.BooleanField()
    allow_resell = models.CharField(max_length=1)
    when_resell = models.CharField(max_length=1, blank=True)
    amount_resell = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title


class Ticket(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    sales_start_date = models.DateField(blank=True, null=True)
    sales_start_time = models.DateTimeField(blank=True, null=True)
    sales_end_date = models.DateField(blank=True, null=True)
    sales_end_time = models.DateTimeField(blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return "Name:"+self.name+" ID:"+str(self.id)