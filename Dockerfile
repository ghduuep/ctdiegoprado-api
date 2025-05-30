# Dockerfile
FROM python:3.12.3-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:8000"]