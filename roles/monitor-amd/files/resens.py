#!/usr/bin/python3
import rocm_smi
import subprocess, re, syslog
count = 0
highest_temp = 0
highest_fan = 0

syslog.openlog("resens")

for device in rocm_smi.listDevices():
  try:
    fan = float(rocm_smi.getFanSpeed(device))
    temp = float(rocm_smi.getSysfsValue(device, 'temp'))
    if ( temp > highest_temp ): highest_temp = temp
    if ( fan > highest_fan ): highest_fan = fan
    count = count + 1
    syslog.syslog("temp" + str(count) + ":" + str(temp))
    syslog.syslog("fan" + str(count) + ":" + str(fan))
  except:
    pass

syslog.syslog("highest_fan:" + str(highest_fan))
syslog.syslog("highest_temp:" + str(highest_temp))
syslog.syslog("gpu_count:" + str(count))
print(str(count))
