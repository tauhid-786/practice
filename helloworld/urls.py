from django.urls import path
from helloworld import views
urlpatterns = [
    path('',views.home),
    path('hello/',views.index),
]
