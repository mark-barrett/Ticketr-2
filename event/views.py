from django.shortcuts import render

# Create your views here.
from django.views import View


class Home(View):

    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        pass
