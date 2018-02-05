from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View

from event.forms import EventForm
from event.models import *

from django.contrib import messages


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
            return redirect('login')

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

                print(name)

                # Check if any of those lists are empty
                if not name or not quantity or not price:
                    messages.error(request, "You must add at least one ticket.")
                    return TemplateResponse(request, "create-event.html", {'form': form})
                else:
                    # Lets loop through each list and see if any of the spaces are empty. If so raise an error

                    for i in range(len(name)):
                        if not name[i] or not quantity[i] or not price[i]:
                            messages.error(request, "There seems to be a problem with a name, quantity or price of one of your tickets.")
                            return TemplateResponse(request, "create-event.html", {'form': form})

                    # We need to get each ticket and save it to the db

                    event.save()

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
            return redirect('login')
