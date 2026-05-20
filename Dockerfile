# Модель: Метод Ньютона (5 семестр)
# Автор: Боденчук Олександр, група АІ-235

FROM python:3.10-slim
WORKDIR /app
COPY main.py .
CMD ["python", "main.py"]
