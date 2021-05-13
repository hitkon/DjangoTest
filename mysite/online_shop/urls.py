from django.urls import path
from . import views

app_name = "online_shop"

urlpatterns=[
    path('', views.index, name="index"),
    #path('')
]
