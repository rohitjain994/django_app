FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /todo_list
WORKDIR /todo_list

ADD requirements.txt /todo_list/
RUN pip install -r requirements.txt

ADD . /django_app/