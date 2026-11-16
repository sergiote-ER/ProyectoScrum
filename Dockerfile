FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ejemplo/ .

RUN mkdir -p /data

EXPOSE 8000

CMD ["gunicorn", "ejemplodjango2.wsgi:application", "--bind", "0.0.0.0:8000"]