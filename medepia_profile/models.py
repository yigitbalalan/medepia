from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authentication import TokenAuthentication


# Create your models here.


class Profile(AbstractUser):
    phone_number = models.CharField(max_length=6,default="+90")
