# coding=utf-8
import time
from sds011 import SDS011
'''
Simple script to put sensor to sleep.
'''

# Create a new sensor instance

'''
On Win, the path is one of the com ports. On Linux / Raspberry Pi
it depends. May be one of "/dev/ttyUSB..." or "/dev/ttyAMA...".
Have a look at Win or Linux documentation.
'''
# Create an instance of your sensor
sensor = SDS011('/dev/ttyUSB0')
sensor.workstate = SDS011.WorkStates.Sleeping
