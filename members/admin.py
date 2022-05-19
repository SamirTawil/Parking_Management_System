from django.contrib import admin

# Register your models here.
from members.models import Members, Etudiant

admin.site.register(Members)
admin.site.register(Etudiant)
