FROM python:3.12

WORKDIR /app

COPY bark/ .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--log-level", "debug", "--reload", "src.server:app"]