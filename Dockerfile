FROM python:2.7-alpine3.7
LABEL AUTHOR="tnajun"

ADD . /app
WORKDIR /app

RUN apk --update add --no-cache --virtual .build-deps mariadb-dev build-base \
    && pip install -r /app/requirements.txt \
    && apk add --virtual .runtime-deps mariadb-client-libs \
    && apk del .build-deps

EXPOSE 5000
CMD python app.py