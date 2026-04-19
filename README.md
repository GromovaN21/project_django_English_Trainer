# English Trainer - Конструктор для изучения слов



Интерактивное веб-приложение на Django для создания словаря иностранных слов и изучения их.



## 🚀 Функционал

*   **Словарь:** Добавление и удаление необходимых слов.

*   **Тест:** Выбор правильного перевода и отображение ошибок.

*   **Карточка:** Выдается карточка на русском нужно вспомнить перевод на английский и перевернуть, чтобы проверить.



## 🛠 Технологии

*   **Backend:** Python 3, Django

*   **Frontend:** HTML5, CSS3, JavaScript



## 📦 Локальная установка и запуск

1. Клонируйте репозиторий: `git clone https://github.com/GromovaN21/project_django_English_Trainer.git`

2. Создайте venv: `python -m venv venv`

3. Активируйте venv: (Powershell) `venv\Scripts\activate.ps1` | (Linux/MacOS Shell) `source venv/bin/activate`de

4. Установите django: `pip install django`

5. Запустите сервер: `python manage.py runserver`



## Docker

### Установка

1. Клонируйте репозиторий:
```
git clone https://github.com/GromovaN21/project_django_English_Trainer.git
```

2. Соберите образ:
```
docker build --no-cache -t english-trainer .
```

3. Запустите образ:
```
docker run --name english-trainer -d -p 80:8000 -e APP_PORT=8000 -e APP_DEBUG=False -v ./data:/app/data english-trainer
```
#### Переменные окружения
* APP_PORT - порт, на котором запускается сервер внутри контейнера. Значение должно соответствовать внутреннему порту аргумента -p команды `docker run`, например, `... -p 80:15672 -e APP_PORT=15672 ...`.
* APP_DEBUG - режим отладки. Включается при значении `... -e APP_DEBUG=True ...` с соблюдением регистра.

### Просмотр логов

Накопленные сообщения на момент запуска команды
```
docker logs english-trainer
```
Отслеживание логов в реальном времени
```
docker logs -f english-trainer
```

### Удаление контейнера с остановкой при необходимости
```
docker rm -f english-trainer
```

### Удаление собранного образа
```
docker image rm english-trainer
```


