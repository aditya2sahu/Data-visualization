from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path("",views.home,name="home"),
    path("Country", views.country, name="country"),
    path("me", views.me, name="me"),
path("letmein", views.letmein, name="letmein"),
path("letmeout", views.letmeout, name="letmeout"),
]
