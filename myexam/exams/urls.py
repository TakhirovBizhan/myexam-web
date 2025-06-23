# exams/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('TBexam/', views.tbexam_list, name='tbexam_list'),
]