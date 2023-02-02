FROM python:3.11
EXPOSE 80

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY .. /app

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "80"]