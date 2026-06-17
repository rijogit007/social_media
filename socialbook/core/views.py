from django.shortcuts import render,redirect

from django.contrib.auth.models import User,auth

from django.contrib import messages

# Create your views here.


def index(request):
    
    return render(request, 'index.html')


def home(request):
    return render (request,'home.html')


def signup(request):

    if request.method == "POST":

        user_name = request.POST.get('user_name')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:

            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('signup')

            elif User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')

            else:
                user = User.objects.create_user(
                    username=user_name,
                    first_name=first_name,
                    email=email,
                    password=password1
                )

                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')

    return render(request, 'signup.html')