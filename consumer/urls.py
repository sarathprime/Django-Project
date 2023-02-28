from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('c_index/', views.c_index),
    path('c_login/', views.c_login),
    path('c_register/', views.c_register),
    path('c_details/', views.c_details),
    path('c_requirement/', views.c_requirement),
    path('C_logout/', views.C_logout),
    path('DELIVERED/', views.DELIVERED),




]