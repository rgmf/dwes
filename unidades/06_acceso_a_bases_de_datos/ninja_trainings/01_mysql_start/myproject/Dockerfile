FROM python:3.12

WORKDIR /app

COPY myproject/ .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "src.main"]