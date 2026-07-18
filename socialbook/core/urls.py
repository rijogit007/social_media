from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    
    path('signup',views.signup,name='signup'),
    path('profile',views.profile,name='profile'),
    path('likepost',views.like_post,name='like_post'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('upload',views.upload,name='upload'),
    path('settings',views.settings,name='settings'),
    path('allimage',views.userallimg,name='allimages'),
    
    
]