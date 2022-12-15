FROM python:3.7-alpine

#RUN addgroup -S pingbot \
# && adduser -S pingbot -G pingbot

ARG API_TOKEN
ARG REMOTE_IP

ENV API_TOKEN=${API_TOKEN}
ENV REMOTE_IP=${REMOTE_IP}

WORKDIR /usr/src/app/

COPY ./src/ ./

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apk add --no-cache linux-headers libc-dev \
    py3-psutil gcc \
 && pip3 install -r requirements.txt

#USER pingbot

CMD [ "python3", "main.py" ]
