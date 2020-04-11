#!/bin/sh
if ps -ef | grep -v grep | grep pox_2_influx.py ; then
        exit 0
else
        /home/pi/Pulse_grafana/pox_2_influx.py &
        exit 0
fi
