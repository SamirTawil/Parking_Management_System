from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
  
    path('administration',views.administration),
    path('etudian',views.etudian),
    path('prof',views.prof),
    path('pe',views.pe),
    path('pf',views.pf),

    path('username',views.username),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),

    path('updatest/updaterecordst/<int:id>', views.updaterecordst, name='updaterecordst'),
    path('addst/', views.addst, name='addst'),
    path('addst/addrecordst/', views.addrecordst, name='addrecordst'),
    path('deletest/<int:id>', views.deletest, name='deletest'),
    path('updatest/<int:id>', views.updatest, name='updatest'),

    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]
