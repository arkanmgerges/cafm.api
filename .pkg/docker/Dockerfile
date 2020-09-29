FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip install -qr requirements.txt

EXPOSE 80
CMD ["uvicorn", "src.port_adapter.api.rest.main:app", "--host", "0.0.0.0", "--port", "80"]
