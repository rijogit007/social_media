from django.shortcuts import render,redirect

from django.contrib.auth.models import User,auth

from django.contrib import messages

# Create your views here.


def index(request):
    
    return render(request, 'index.html')



def signup(request,id):
    
    if request.method=="POST":
        
        username=request.POST['firstname']
        email=request.POST['email']
        password1=request.POST['password1']    
        password2=request.POST['password2']
        
        
        if password1==password2:   
            if User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                
            elif  User.objects.filter(username=username).exists():
                
                messages.info(request,'username already taken')
                
            else:
                
                user=User.objects.create_user(username=username,password=password1)
                user.save()    
                
        else:
            
            messages.info(request,"password not matching")  
            return redirect('signup')  
    else:        
                 
    
        return render(request,'signup.html')