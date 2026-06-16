from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


User=get_user_model()


class Profile(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=
    bio=
    profileimg=models.ImageField(upload_to='profile_images')