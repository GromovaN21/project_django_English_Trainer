"""Главная страница приложения"""
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST

from .models import DictionaryRecord

def index(request):
    """Отображает главную страницу с конструктором фигур."""
    return render(request, 'cards/index.html')

@require_POST
def newRecord(request):
    en = request.POST['word-en']
    ru = request.POST['word-ru']
    DictionaryRecord.objects.create(english=en, russian=ru)
    return JsonResponse({'status': 'ok'})

@require_POST
def deleteRecord(request, pk):
    obj = get_object_or_404(DictionaryRecord, pk=pk)
    obj.delete()
    return JsonResponse({'status': 'ok', 'id': pk})

def recordsJson(request):
    qs = DictionaryRecord.objects.all().order_by('russian')
    data = [
        {'id': o.pk, 'ru': o.russian, 'en': o.english}
        for o in qs
    ]
    return JsonResponse({'records': data})
        