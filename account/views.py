from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


class SignIn(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # Get the post information
        pass


class SignUp(View):

    def get(self, request):
        pass

    def post(self, request):
        pass

class ForgotPassword(View):

    def get(self, request):
        pass

    def post(self, request):
        pass
