#!/bin/bash

# For some reason after rebooting my raspberry, the sensor is not initialized correctly, 
# which breaks scripts for first 3 times they are run. We will work around this by trying 
# to put the sensor to sleep for 3 times just after booting up (via cron). The forth call 
# is actually putting the sensor to sleep after reboot which is useful for saving 
# the laser life.

MY_PATH="`dirname \"$0\"`"

echo $(date) "Sensor reconnected. Trying to put it to sleep..." >> $MY_PATH/reconnect.log

sleep 10 #wait to make sure devices is initialized

timeout 15s python3 $MY_PATH/put_to_sleep.py
sleep 5
timeout 15s python3 $MY_PATH/put_to_sleep.py
sleep 5
timeout 15s python3 $MY_PATH/put_to_sleep.py
sleep 5
timeout 15s python3 $MY_PATH/put_to_sleep.py

echo $(date) "Reconnecting finished." >> $MY_PATH/reconnect.log
