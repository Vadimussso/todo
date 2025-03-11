FROM python:3.10-slim

WORKDIR /app

RUN adduser --disabled_password --geos "" appuser

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.in .
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

COPY . .

USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]