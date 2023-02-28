from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('molding_index/', views.molding_index),
    path('m_login/', views.m_login),
    path('m_register/', views.m_register),
    path('view_Admin/', views.view_Admin),
    path('view_table/', views.view_table),
    path('m_need/', views.m_need),
    path('analysing/', views.analysing),
    path('Teaam_register/', views.Teaam_register),
    path('get_inputs/<int:id>/', views.get_inputs),
    path('view_dropped/', views.view_dropped),
    path('molding_process/', views.molding_process),
    path('molded_products/', views.molded_products),
    path('M_logout/', views.M_logout),


]