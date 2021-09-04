from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name = "home" ),
    path('about', views.about, name = "abouts"),
    path('create', views.create, name = "creates")
]
