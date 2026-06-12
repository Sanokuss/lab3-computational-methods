# Модель: Метод Ньютона (5 семестр)
# Автор: Боденчук Олександр, група АІ-235

FROM python:3.10-slim
WORKDIR /app

# 1. Спочатку копіюємо файл із залежностями
COPY requirements.txt .

# 2. Встановлюємо Flask (та інші бібліотеки, якщо будуть)
RUN pip install --no-cache-dir -r requirements.txt

# 3. Копіюємо сам код програми
COPY main.py .

# 4. Запускаємо сервер
CMD ["python", "main.py"]
