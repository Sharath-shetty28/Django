from django.urls import path
from . import views

urlpatterns = [
    path('merge_pdf/', views.merge_pdfs, name='merge_pdfs'),
    path('merge_word/', views.merge_words, name='merge_words'),
    path('', views.index, name='index'),
]
