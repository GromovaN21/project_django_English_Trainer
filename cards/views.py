"""Главная страница приложения"""
from django.shortcuts import render

def index(request):
    """Отображает главную страницу с конструктором фигур."""
    return render(request, 'cards/index.html')
