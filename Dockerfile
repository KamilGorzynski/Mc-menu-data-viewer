FROM python:3.8.0b3-slim as base

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
COPY /config.py /config.py
COPY /alembic /alembic
COPY /alembic.ini /alembic.ini

WORKDIR /

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=true
ENV FLASK_ENV=development



