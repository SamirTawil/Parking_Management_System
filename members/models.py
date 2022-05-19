from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    batiment = models.CharField(max_length=255)
    nbr = models.CharField(max_length=255, default=None, blank=True, null=True)


class Members(MyUser):
    class Meta:master
        proxy = True


class Etudiant(MyUser):
    class Meta:
        proxy = True
