FROM python:3.9-alpine3.13
LABEL maintainer="askolenko"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ../../requirements.dev.txt /tmp/requirements.dev.txt
COPY ../../requirements.txt /tmp/requirements.txt
RUN python -m venv /py && \
   /py/bin/pip install --upgrade pip && \
   apk add --update alpine-sdk && \
   apk add --update --no-cache postgresql-client && \
   apk add --update --no-cache --virtual .tmp-build-deps \
      build-base gcc python3-dev postgresql-dev musl-dev libffi-dev openssl-dev cargo  && \
   /py/bin/pip install -r /tmp/requirements.dev.txt && \
   /py/bin/pip install -r /tmp/requirements.txt && \
   rm -rf /tmp && \
   adduser \
       --disabled-password \
       --no-create-home \
       ecommerce_user

COPY ../.. .
WORKDIR /backend
EXPOSE 8000


ENV PATH="/py/bin:$PATH"


USER ecommerce_user