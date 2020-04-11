# Masimo Rad-8 Pulse Oximeter Data to InfluxDB

A simple Python3 script to read serial data from a Masimo Rad-8 Pulse Oximeter. Samples are taken
at a frequency of 1 sample/second, put in JSON format and sent to a local influxDB instance. This
data is visualized using Grafana.

## Purpose

My daughter has a trach and is ventilator dependent. My wife and I need to watch her O2 percentages
and were only able to do so if we were sitting in front of the pulse oximeter. Now, using influxDB 
and Grafana running on a local server, we can see her specific oxygen and heartrate from anywhere in
our home.

## Grafana Dashboard for Pulse Oximeter Data w/ Inside Weather

![alt text](pulse_grafana_screenshot1.png)

## How to Use

These scripts are installed on a Raspberry Pi Zero W running Debian Buster Lite. The Pi is strapped
to my daughters pulse oximeter which is sometimes mobile. Due to the pulse oximeter and Pi being
mobile, I energize the Pi using a cell phone battery charger. Because the charge is not infinite and I
do not want to hook the pi up to a monitor or ssh in every power cycle, I use a keep_going script. The
keep_going script has been setup to run every minute as a cronjob. If the keep_going script sees
pox_2_influx running in the background, nothing is done and keep_going will exit. If pox_2_influx is not
running, then it will be executed. Please change the path w/in graf_keep_going.sh to reflect the location
of pox_2_influx.py.

The two primary files are:

1. pox_2_influx.py
2. graf_keep_going.sh
