FROM python:3.14-slim

RUN mkdir -p /app/data
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate

EXPOSE $APP_PORT

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:$APP_PORT"]
