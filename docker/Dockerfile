FROM python:3.7-alpine

ARG API_TOKEN
ARG REMOTE_IP

ENV API_TOKEN=${API_TOKEN}
ENV REMOTE_IP=${REMOTE_IP}

WORKDIR /usr/src/app/

COPY ./src/ ./
RUN apk add --no-cache linux-headers libc-dev \
    py3-psutil gcc \
 && pip3 install -r requirements.txt

CMD [ "python3", "main.py" ]
