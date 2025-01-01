from django.urls import path
from . import views

urlpatterns = [
    path('img_to_pdf/', views.img_to_pdf, name='img_to_pdf'),
    path('word_to_pdf/', views.word_to_pdf, name='word_to_pdf'),
]
