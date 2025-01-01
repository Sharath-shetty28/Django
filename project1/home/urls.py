from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),

    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
]
