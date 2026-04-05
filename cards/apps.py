"""Модуль конфигурации приложения cards."""
from django.apps import AppConfig

class CardsConfig(AppConfig):
    """Класс конфигурации для приложения карточек."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cards'
