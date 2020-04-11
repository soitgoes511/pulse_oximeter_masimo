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
