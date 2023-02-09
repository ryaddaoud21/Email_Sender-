from django.contrib import admin
from django.urls import path, include
from .views import  ContactView ,ContactSuccessView
urlpatterns = [
    path('', ContactView.as_view(), name="contact"),
    path('success/', ContactSuccessView.as_view(), name="success"),

]
