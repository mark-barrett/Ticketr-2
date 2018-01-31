from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View

from event.forms import EventForm
from event.models import *


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
        pass
