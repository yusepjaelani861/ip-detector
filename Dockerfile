FROM python:3.12.2
COPY /app /app
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "4040"]