from django.shortcuts import render

# Create your views here.
from django.views import View


class Home(View):

    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        pass


class CreateEvent(View):

    def get(self, request):
        return render(request, 'create-event.html')

    def post(self, request):
        pass
