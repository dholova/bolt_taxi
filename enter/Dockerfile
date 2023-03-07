FROM python:3
ENV PYTHONDONTWRITYBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /enter
ADD . /enter
#COPY ./requirements.txt /enter/requirements.txt
RUN pip install django
COPY . /enter

