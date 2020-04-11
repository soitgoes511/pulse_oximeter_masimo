# Import serial package to open and read from masimo rad-8 serial port
import serial
from datetime import datetime
from influxdb import InfluxDBClient

# Serial device mounted at /dev/ttyUSB0 with a 9600 baudrate
ser    = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)
sample = []
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('pulse_readings')

while True:
    sample = ser.readline().decode('utf-8').split()
    if len(sample) > 5:
        date   = sample[0]
        time   = sample[1]
        sn     = int(sample[2].lstrip('SN='))
        dttm   = date + ' ' + time
        dttm   = datetime.strptime(dttm, '%m/%d/%y %H:%M:%S')
        spo2   = sample[3]
        spo2   = int(spo2.lstrip('SPO2=').rstrip('%'))
        bpm    = sample[4]
        bpm    = int(bpm.lstrip('BPM='))

        json_body = [
                {
                    "measurement": "spo2",
                    "tags": {
                        "serialnum": sn
                        },
                    "time": dttm,
                    "fields": {
                        "spo2": spo2,
                        "bpm": bpm
                        }
                    }
                ]
        client.write_points(json_body)

    else:
        pass
