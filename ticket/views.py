from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from event.models import Ticket


class Order(View):

    def get(self, request):
        return redirect('/')

    def post(self, request):
        # Get the list of tickets and quantities
        tickets = request.POST.getlist('tickets')
        quantities = request.POST.getlist('quantities')

        has_quantifiable_tickets = False

        for quantity in quantities:
            if int(quantity) is not 0:
                has_quantifiable_tickets = True

        if has_quantifiable_tickets:
            # Create ticket list for all of tickets.
            ticket_list = []

            # Loop through the quantities and if they are 0 don't add them to the ticket list
            for index, quantity in enumerate(quantities):
                if int(quantity) is not 0:
                    db_ticket = Ticket.objects.get(id=tickets[index])
                    fees = round((((float(db_ticket.price) / 100) * 2.5) + 1.99), 2)

                    ticket_obj = {
                        'ticket': db_ticket,
                        'quantity': quantity,
                        'fees': fees,
                        'sub_total': round((float(db_ticket.price) + fees) * float(quantity), 2)
                    }
                    ticket_list.append(ticket_obj)

            # Hardcoded until post is ready
            context = {
                'ticket_list': ticket_list,
                'event': Ticket.objects.get(id=tickets[1]).event
            }

            return render(request, 'order.html', context)
        else:
            messages.warning(request, "You must pick at least 1 ticket.")
            return redirect('/event/'+request.POST['event'])
