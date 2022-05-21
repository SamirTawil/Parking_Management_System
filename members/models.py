from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    role = models.CharField(choices=[("Student", "Student"), ("Professor", "Professor")], max_length=30, null=True,
                            default="Student")


class ParkingSpot(models.Model):
    batiment = models.CharField(choices=[("ESIB", "ESIB"), ("FS", "FS"), ("IGE", "IGE")], max_length=255)
    nbr = models.CharField(max_length=255, default=None, blank=True, null=True)
    user = models.OneToOneField(to=MyUser, on_delete=models.CASCADE, null=True, blank=True)
