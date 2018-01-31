from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


class SignIn(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        pass
