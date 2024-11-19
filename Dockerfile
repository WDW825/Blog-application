# Используем официальный образ Python
FROM python:3.10

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

#CMD ["sh", "-c", "cd /app/Blog && python manage.py runserver 0.0.0.0:8000"]
