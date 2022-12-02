#!/usr/bin/env bash

# Debian-like only OS support, other OS will be added soon.

systemctl --version && echo "OK, proceed" || echo "Systemd is not installed, exit" exit 1

WORKDIR="/opt/ping_bot/"
mkdir -p ${WORKDIR}
cp ./src/main.py ${WORKDIR}

cp ./linux/ping_bot.service /etc/systemd/system/ping_bot.service
systemctl daemon-reload
systemctl enable ping_bot.servive
systemctl start ping_bot.service
