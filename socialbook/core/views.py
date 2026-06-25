from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from core.models import Profile
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
                
            user_login=auth.authenticate(username=user_name,password=password1,email=email)
            auth.login(request,user_login)    
                
            user_model=User.objects.get(username=user_name)
            
            new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
            
            new_profile.save()
        
            return redirect('signin')

        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')

    return render(request, 'signup.html')



def signin(request):
    
    if request.method=="POST":
        
        username=request.POST["user_name"]
        password=request.POST["password1"]
        
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        
        else:
            messages.info(request, 'check credential')
            return redirect('signin')
            
            
        
    return render(request,'signin.html')



def logout(request):
    
    auth.logout(request)
    return render(request,'index.html')


@login_required(login_url='signin')
def settings(request):
    setting = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        profileimg = request.FILES.get('profileimg')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        bio = request.POST.get('bio')
        location = request.POST.get('location')

        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.save()

        setting.bio = bio
        setting.location = location

        if profileimg:
            setting.profileimg = profileimg

        setting.save()

    return render(request, 'settings.html', {'setting': setting})


