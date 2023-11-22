FROM python:3.10.0b3-slim as base

RUN pip install --no-cache-dir --upgrade -U pip

FROM base as builder

RUN mkdir /install

WORKDIR /install

COPY /requirements.txt /requirements.txt

RUN pip install --prefix=/install -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local

COPY /blueprints /blueprints
COPY /wsgi.py /wsgi.py
COPY /app.py /app.py

WORKDIR /

ENV FLASK_APP=wsgi

CMD gunicprn wsgi -w 2 --timeout 480 --bind 0.0.0.0:80


