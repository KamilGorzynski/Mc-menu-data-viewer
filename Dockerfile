FROM python:3.8.0b3-slim as base

RUN pip install --no-cache-dir --upgrade -U pip

FROM base as builder

RUN mkdir /install

WORKDIR /install

COPY /requirements.txt /requirements.txt

RUN pip install --prefix=/install -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local

RUN mkdir /src

COPY . /src

WORKDIR /src

ENV PYTHONBUFFERED 1
ENV FLASK_APP=/src/app/wsgi.py
ENV FLASK_DEBUG=true
ENV FLASK_ENV=development



