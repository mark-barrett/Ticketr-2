from django.shortcuts import render

# Create your views here.
from django.views import View

from event.models import Ticket


class Order(View):

    def get(self, request, ticket_id):

        # Get ticket
        ticket = Ticket.objects.get(id=ticket_id)

        context = {
            'ticket': ticket
        }

        return render(request, 'order.html', context)
