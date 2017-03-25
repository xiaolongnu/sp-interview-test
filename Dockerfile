FROM python:2-onbuild
RUN mkdir /code
WORKDIR /code
ADD . /code/