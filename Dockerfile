# Stage 1: build dependencies
FROM python:3.11-slim AS builder
WORKDIR /app

# Установка зависимостей для сборки (если нужны)
RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip wheel --no-deps --wheel-dir=/wheels -r requirements.txt

# Stage 2: final image
FROM python:3.11-slim
WORKDIR /app

# (опционально) системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*

COPY --from=builder /wheels /wheels
RUN pip install --no-index --find-links=/wheels -r requirements.txt

# Копируем приложение
COPY . .

# Указываем порт/команду — подставь реальную команду старта
EXPOSE 8000
CMD ["python", "main.py"]
