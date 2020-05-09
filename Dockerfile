FROM python:3.8.0-alpine

WORKDIR /usr/src/recetapp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip

RUN apk add zlib libjpeg-turbo-dev libpng-dev freetype-dev lcms2-dev libwebp-dev harfbuzz-dev fribidi-dev tcl-dev tk-dev

COPY ./requirements.txt /usr/src/recetapp/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/recetapp/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
