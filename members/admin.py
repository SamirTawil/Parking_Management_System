from django.contrib import admin

# Register your models here.
from members.models import MyUser, ParkingSpot

admin.site.register(MyUser)
admin.site.register(ParkingSpot)
