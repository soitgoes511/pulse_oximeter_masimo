#!/usr/bin/python3

import smbus2
import bme280
from influxdb import InfluxDBClient

port = 1
address = 0x77
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

client = InfluxDBClient(host='192.168.0.6', port=8086)
client.switch_database('pulse_readings')

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

temp = (data.temperature * (9/5) + 32)

json_body = [
        {
            "measurement": "bme280",
            "tags": {
                "id": data.id
                },
            "dttm": data.timestamp,
            "fields": {
                "temperature": temp,
                "pressure": data.pressure,
                "humidity": data.humidity
                }
        }
]

client.write_points(json_body)
#print(json_body)

# the compensated_reading class has the following attributes
#print(data.id)
#print(data.timestamp)
#print(data.temperature * (9/5) + 32)
#print(data.pressure)
#print(data.humidity)

# there is a handy string representation too
#print(data)
