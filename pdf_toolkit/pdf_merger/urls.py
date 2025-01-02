from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('merge_pdfs/', views.merge_pdfs, name='merge_pdfs'),
    path('merge_words/', views.merge_words, name='merge_words'),
    path('', views.index, name='index'),
]
