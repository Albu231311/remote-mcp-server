FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

# Render sets PORT automatically; default to 8080 for local testing
EXPOSE 8080

CMD ["python", "server.py"]
