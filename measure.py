# coding=utf-8
'''
Simple script that reports current time and PM 2.5/10 values.

The script uses SDS011 library provided by Frank Heuer and 
is roughly based on the test.py script provided by Frank.

https://gitlab.com/frankrich/sds011_particle_sensor
'''

import time
from sds011 import SDS011
import logging
import logging.handlers

# Create a new sensor instance

'''
On Win, the path is one of the com ports. On Linux / Raspberry Pi
it depends. May be one of "/dev/ttyUSB..." or "/dev/ttyAMA...".
Have a look at Win or Linux documentation.
'''
# Create an instance of your sensor
sensor = SDS011('/dev/ttyUSB0')
sensor.dutycycle = 0 #TODO what values is reasonable here?
sensor.workstate = SDS011.WorkStates.Measuring
# Wait 60 seconds to get right values. Sensor has to warm up! #TODO is this really the case?
time.sleep(60)

pm25 = []
pm10 = []

for a in range(60):
	while True:
		values = sensor.get_values()
		if values is not None:
			pm25.append(values[1])
			pm10.append(values[0])
			break

pm25_avg = sum(pm25) / len(pm25)
pm10_avg = sum(pm10) / len(pm10)

if values is not None:
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),",", "{0:.1f}".format(pm10_avg), ",", "{0:.1f}".format(pm25_avg))

time.sleep(10)
sensor.workstate = SDS011.WorkStates.Sleeping
time.sleep(10)
