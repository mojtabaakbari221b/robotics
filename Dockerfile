FROM python:3.9
LABEL MAINTAINER="inolinX | https://quiz.noarino.ir"
LABEL VERSION="0.0.0.1"

ENV PYTHONUNBUFFERED 1

ENV HOME=/opt/robomech/

# Set working directory
RUN mkdir -p $HOME
WORKDIR $HOME

# Installing requirements
COPY * $HOME

RUN pip install -r base.txt
RUN pip install --upgrade pip
