# Pull base Image

FROM python:3.8


#Set Environment Variable

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set Work Directory

WORKDIR /code

#Install Dependencies

COPY Pipfile Pipfile.lock /code/

RUN pip install pipenv && pipenv install --system

#Copy project

COPY . /code/