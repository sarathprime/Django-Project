from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin_login/', views.admin_login),
    path('a_index/', views.a_index),
    path('view_stock/', views.view_stock),
    path('view_client/', views.view_client),
    path('find_raw/', views.find_raw),
    path('Request/', views.Request),
    path('loading/', views.loading),
    path('send_m/', views.send_m),
    path('view_payment/', views.view_payment),
    path('credit_card/', views.credit_card),
    path('get_input/<int:id>/', views.get_input),
    path('C_stock/<int:id>/', views.C_stock),
    path('C_fr/<int:id>/', views.C_fr),
    path('final_payment/', views.final_payment),
    path('A_logout/', views.A_logout),

]