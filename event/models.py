from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class Organiser(models.Model):

    name = models.CharField(max_length=256)
    about = models.TextField()
    image = models.ImageField(upload_to='static/organiser_images', blank=True, null=True)
    website = models.CharField(max_length=256)
    facebook = models.CharField(max_length=256)
    twitter = models.CharField(max_length=256)
    background_colour = models.CharField(max_length=10)
    text_color = models.CharField(max_length=10)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Organisers'

    def __str__(self):
        return self.name


class Event(models.Model):

    title = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    start_date = models.DateField()
    start_time = models.DateField()
    end_date = models.DateTimeField()
    end_time = models.DateTimeField()
    image = models.ImageField(upload_to='static/event_images', blank=True, null=True)
    description = models.TextField()
    organiser = models.ForeignKey(Organiser)
    privacy = models.CharField(max_length=1)
    show_remaining_tickets = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title


class Ticket(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    sales_start_date = models.DateField()
    sales_start_time = models.DateTimeField()
    sales_end_date = models.DateField()
    sales_end_time = models.DateTimeField()
    event = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return "Name:"+self.name+" Event: "+self.event.title+" ID:"+str(self.id)