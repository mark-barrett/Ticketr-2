from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.views import View


class SignIn(View):

    def get(self, request):

        if not request.user.is_authenticated:
            return render(request, 'sign-in.html')
        else:
            return redirect('/')

    def post(self, request):
        # Get the post information
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate the user with their email as the username
        user = authenticate(username=email, password=password)

        # Check if the user logged in okay
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'The email or password is invalid.')
            return redirect('/account/sign-in')


class SignUp(View):

    def get(self, request):
        if not request.user.is_authenticated():
            return render(request, 'sign-up.html')
        else:
            return redirect('/')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

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

                user.save()  # DO NOT FORGET THIS LINE

                # Check if the user logged in okay
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Your account has been setup.')
                    return redirect('/')
                else:
                    messages.error(request, 'There was an error signing up')
                    return redirect('/account/sign-up')


class SignOut(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "Logged out. Thanks for stopping by!")
            return redirect('/')


class ForgotPassword(View):

    def get(self, request):
        pass

    def post(self, request):
        pass
