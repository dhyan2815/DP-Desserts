from django.contrib import admin
from django.urls import path
from app import views

admin.site.site_header = "DP's Admin Panel"
admin.site.site_title = "DP's Desserts"
admin.site.index_title = "DP's Access Control"

urlpatterns = [
    path('', views.index, name='Home'),
    path('home', views.index, name='Home'),

    path('about', views.about, name='About'),

    path('menu', views.menu, name='Menu'),
    
    path('order', views.order, name='order'),

    path('order_confirmation', views.order_confirmation, name='order_confirmation')
]