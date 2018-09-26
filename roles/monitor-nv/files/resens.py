#!/usr/bin/python3
import subprocess, re, syslog
syslog.openlog("resens")
count = -1
highest_temp = 0
highest_fan = 0
data = subprocess.check_output(['nvidia-smi', '--list-gpus'])
for line in data.decode().split('\n'):
  if re.search(r'\GPU\b', line):
    count = count + 1
    try:
      temp = float(subprocess.check_output('nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits -i ' + str(count), shell=True))
      fan = float(subprocess.check_output('nvidia-smi --query-gpu=fan.speed --format=csv,noheader,nounits -i ' + str(count), shell=True))
      if ( temp > highest_temp ): highest_temp = temp
      if ( fan > highest_fan ): highest_fan = fan
      syslog.syslog("temp" + str(count + 1) + ":" + str(temp))
      syslog.syslog("fan" + str(count + 1) + ":" + str(fan))
    except:
      pass
syslog.syslog("highest_fan:" + str(highest_fan))
syslog.syslog("highest_temp:" + str(highest_temp))
syslog.syslog("gpu_count:" + str(count+1))
print(str(count+1))
