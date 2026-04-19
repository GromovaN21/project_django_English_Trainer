"""Импорт моделей"""
from django.db import models

class DictionaryRecord(models.Model):
  english = models.CharField(max_length=50, unique=True)
  russian = models.CharField(max_length=50, unique=True)