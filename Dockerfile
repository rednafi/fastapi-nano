
FROM python:3.8.3-slim-buster


RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt
EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
