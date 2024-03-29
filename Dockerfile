FROM python:3.6-alpine

RUN mkdir -p /usr/src/app \
 && mkdir -p /usr/src/app/files

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apk add ffmpeg

RUN pip3 install --no-cache-dir -r requirements.txt
RUN apk add --no-cache ffmpeg

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]