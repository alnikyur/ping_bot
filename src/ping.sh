#!/bin/sh

PING_=$(ping -q -4 -c 4 ${REMOTE_IP} | grep -i loss | awk '{print $7}')

if [ ${PING_} == "0%" ]; then
	echo "OK, the power is up =)"
else
	echo "No electricity =("
fi
