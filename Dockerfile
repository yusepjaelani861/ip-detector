FROM python:3.12.2
COPY /app /app
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["python", "main.py"]