from django.contrib import messages
from django.contrib.auth.models import User
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

            total = 0

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
                    total += round((float(db_ticket.price) + fees) * float(quantity), 2)

            # Hardcoded until post is ready
            context = {
                'ticket_list': ticket_list,
                'event': Ticket.objects.get(id=tickets[1]).event,
                'total': total
            }

            return render(request, 'order.html', context)
        else:
            messages.warning(request, "You must pick at least 1 ticket.")
            return redirect('/event/'+request.POST['event'])


class ConfirmOrder(View):

    def get(self, request):
        return redirect('/')


    def post(self, request):
        # Check if the user needs to be registered
        if request.POST['register'] == 'yes':
            # The user does have to be registered
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']

            ticket_ids = request.POST.getlist('ticket_ids')
            quantities = request.POST.getlist('ticket_quantities')

            # So lets register them!
            # Try find the user to see if they exist
            try:
                db_user = User.objects.get(username=email)

                messages.error(request, 'A user with that email already exists.')
                return redirect('/account/sign-up')
            except:
                user, created = User.objects.get_or_create(username=email, email=email)
                if created:
                    user.set_password(password)  # This line will hash the password

                    user.first_name = first_name
                    user.last_name = last_name

                    user.save()

                    # Check if the user has been saved.
                    if user is not None:
                        # Now they have been created then lets create orders that will then be confirmed later.
                        # First we need to create an order entry.
                        order = Order(

                        )

                    else:
                        messages.error(request, 'There was an error signing up')
                        return redirect('/account/sign-up')



        else:
            # The user does not have to be registered
            ticket_ids = request.POST.getlist('ticket_ids')
            quantities = request.POST.getlist('ticket_quantities')


