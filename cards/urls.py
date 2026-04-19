"""Главная страница приложения"""
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add-record', views.newRecord, name="add-record"),
    path('records/', views.recordsJson, name="records-json"),
    path('records/<int:pk>/delete/', views.deleteRecord, name="delete-record")
]
