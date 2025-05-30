FROM python:3.12.3-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Não fixar a porta aqui
EXPOSE $PORT

# Usar a variável PORT do Railway
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT seu_projeto.wsgi:application"]