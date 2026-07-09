FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
COPY requirements-gcp.txt .
RUN pip install --no-cache-dir -r requirements-gcp.txt
COPY src/ ./src/
# Cloud Run HTTP entrypoint (weekly Scheduler hits this URL)
ENV FUNCTION_TARGET=handler
CMD exec functions-framework --source=src/main.py --target=handler --port=${PORT:-8080}
