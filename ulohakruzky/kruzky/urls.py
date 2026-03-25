from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index' ),
    path('pridaj/', views.pridaj_kruzok, name='pridaj_kruzok'),
]