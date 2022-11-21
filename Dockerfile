FROM python:3.7-alpine

ARG API_TOKEN
ARG ROUTER_IP

ENV API_TOKEN=${API_TOKEN}
ENV ROUTER_IP=${ROUTER_IP}

WORKDIR /usr/src/app/

COPY . .
RUN apk add linux-headers libc-dev --no-cache
RUN apk add --no-cache py3-psutil gcc && \
    pip3 install -r requirements.txt

CMD [ "python3", "bot.py" ]
