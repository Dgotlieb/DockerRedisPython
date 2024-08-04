FROM python:3.7-alpine
COPY . /code
WORKDIR /code
RUN pip install flask
RUN pip install redis
RUN chmod 644 app.py
CMD ["python", "app.py"]
