# Dockerfile for demo-api
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app
COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]
