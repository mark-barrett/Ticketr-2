import datetime

from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View

from event.forms import EventForm, TicketForm
from event.models import *

from django.contrib import messages

from ticket.models import Order, OrderTicket


class Home(View):

    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        pass


class CreateEvent(View):
    model = Event
    fields = '__all__'
    template_name = 'create-event.html'

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'form': EventForm(request=request)
            }
            return TemplateResponse(request, "create-event.html", context)
        else:
            return redirect('/account/sign-in')

    def post(self, request):
        if request.user.is_authenticated:
            form = EventForm(request.POST, request.FILES, request=request)
            if form.is_valid():
                event = form.save(commit=False)
                # commit=False tells Django that "Don't send this to database yet.
                # I have more things I want to do with it."

                # We need to check if tickets were added
                name = request.POST.getlist('name')
                quantity = request.POST.getlist('quantity')
                price = request.POST.getlist('price')

                # Check if any of those lists are empty
                if not name or not quantity or not price:
                    messages.error(request, "You must add at least one ticket.")
                    return TemplateResponse(request, "create-event.html", {'form': form})
                else:
                    # Lets loop through each list and see if any of the spaces are empty. If so raise an error

                    # We need to get each ticket and save it to the db
                    for i in range(len(name)):
                        if not name[i] or not quantity[i] or not price[i]:
                            messages.error(request, "There seems to be a problem with a name, quantity or price of one of your tickets.")
                            return TemplateResponse(request, "create-event.html", {'form': form})

                    # Check if the event date and time are not already over
                    if event.start_date < datetime.datetime.now().date():
                        messages.error(request, "Your start date cannot have already happened.")
                        return TemplateResponse(request, "create-event.html", {'form': form})
                    else:
                        # Check if the start date is past the end date
                        if event.start_date > event.end_date:
                            messages.error(request, "Your start date is ahead of your end date.")
                            return TemplateResponse(request, "create-event.html", {'form': form})
                        else:
                            event.save()

                    # event.save()

                    for i in range(len(name)):
                        ticket = Ticket(name=name[i],
                                        quantity=quantity[i],
                                        price=price[i],
                                        event=event)

                        ticket.save()

                    messages.success(request, "Event successfully created.")
                    return redirect('/')
            else:
                return TemplateResponse(request, "create-event.html", {'form': form})
        else:
            return redirect('/account/sign-in')


class MyEvents(View):

    def get(self, request):
        if request.user.is_authenticated:
            # Get all of the users organiser profiles
            organiser_profiles = Organiser.objects.all().filter(user=request.user)

            # Now get all of the events belonging to those organisers.
            events = Event.objects.all().filter(organiser__in=organiser_profiles)

            context = {
                'events': events
            }

            return render(request, 'my-events.html', context)
        else:
            return redirect('/account/sign-in')

    def post(self, request):
        pass


class ViewEvent(View):


    def get(self, request, event_id):

        event = Event.objects.get(id=event_id)

        tickets = Ticket.objects.all().filter(event=event)

        for ticket in tickets:
            if ticket.price > 0:
                free_event = False
            else:
                free_event = True

        context = {
            'event': event,
            'tickets': tickets,
            'free_event': free_event
        }

        return render(request, 'view-event.html', context)

    def post(self, request):
        pass


class ManageEvent(View):

    def get(self, request, event_id):
        if request.user.is_authenticated:

            event = Event.objects.get(id=event_id)

            tickets_sold = OrderTicket.objects.all().filter(event=event).count()

            # Get the available tickets in the event
            available_tickets = 0

            tickets = Ticket.objects.all().filter(event=event)

            for ticket in tickets:
                available_tickets += ticket.quantity

            # Calculate the percentage sold for the bar.
            percentage_sold = (100/available_tickets) * tickets_sold

            if event.organiser.user == request.user:
                context = {
                    'event': event,
                    'recent_orders': Order.objects.all().filter(event=event, status=True).order_by('-id')[:4],
                    'tickets_sold': tickets_sold,
                    'available_tickets': available_tickets,
                    'percentage_sold': percentage_sold
                }

                return render(request, 'manage-event.html', context)
            else:
                return redirect('/event/my-events')
        else:
            return redirect('/account/sign-in')


class ManageTickets(View):

    def get(self, request, event_id):
        if request.user.is_authenticated:

            event = Event.objects.get(id=event_id)

            if event.organiser.user == request.user:
                context = {
                    'event': event,
                    'tickets': Ticket.objects.all().filter(event=event)
                }

                return render(request, 'manage-tickets.html', context)
            else:
                return redirect('/event/my-events')
        else:
            return redirect('/account/sign-in')


class CreateTicket(View):

    model = Ticket
    fields = '__all__'
    template_name = 'create-ticket.html'

    def get(self, request, event_id):
        if request.user.is_authenticated:

            event = Event.objects.get(id=event_id)

            if event.organiser.user == request.user:
                context = {
                    'event': event,
                    'form': TicketForm(request=request)
                }
                return TemplateResponse(request, "create-ticket.html", context)
            else:
                return redirect('/event/my-events')
        else:
            return redirect('/account/sign-in')

    def post(self, request, event_id):
        if request.user.is_authenticated:

            event = Event.objects.get(id=event_id)

            if event.organiser.user == request.user:
                form = TicketForm(request.POST, request.FILES, request=request, event=event)
                if form.is_valid():
                    ticket = form.save(commit=False)
                    # commit=False tells Django that "Don't send this to database yet.
                    # I have more things I want to do with it."

                    ticket.event = event

                    ticket.save()

                    messages.success(request, "Event successfully created.")
                    return redirect('/event/manage/tickets/'+event_id)
                else:
                    print(form.errors)
                    return TemplateResponse(request, "create-ticket.html", {'form': form, 'event': event})
        else:
            return redirect('/account/sign-in')


class ListEvents(View):

    def get(self, request):

        context = {
            'events': Event.objects.all()
        }

        return render(request, 'list-events.html', context)

    def post(self, request):
        search_query = request.POST['search_query']

        context = {
            'events': Event.objects.all().filter(Q(title__contains=search_query) | Q(location__contains=search_query))
        }

        return render(request, 'list-events.html',context)


class OrganiserProfiles(View):

    def get(self, request):

        user = User.objects.get(id=request.user.id)

        context = {
            'organisers': Organiser.objects.all().filter(user=user)
        }
        return render(request, 'organiser-profiles.html', context)


class OrganisersProfile(View):

    def get (self, request, organiser_id):

        organiser = Organiser.objects.get(id=organiser_id)

        context = {
            'organiser': organiser,
            'events': Event.objects.all().filter(organiser=organiser)
        }

        return render(request, 'organisers-profile.html', context)


class ViewEventOrders(View):

    def get(self, request, event_id):
        if request.user.is_authenticated:
            # Check to see if the user can see these events.
            event = Event.objects.get(id=event_id)

            user = User.objects.get(id=request.user.id)

            if user == request.user:

                context = {
                    'event': event,
                    'orders': Order.objects.all().filter(event=event, status=True)
                }

                return render(request, 'manage-orders.html', context)
            else:
                return redirect('/event/my-events')
        else:
            return redirect('/account')