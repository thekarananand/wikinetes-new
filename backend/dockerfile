FROM python:3.12-alpine

COPY . /opt/wikinetes/backend

WORKDIR /opt/wikinetes/backend

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]