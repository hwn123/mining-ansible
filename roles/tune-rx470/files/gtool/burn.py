import subprocess
import syslog
import sys
import time
if __name__ == '__main__':
#Array for memory clocks
    cclocks = []
#1 - internal gpu present, 0 - no internal gpu
    igpu = 0
#mclock.conf for memory clock settings
    with open('mclock.conf', 'r') as conf:
        data = conf.read()
        for line in data.split('\n'):
            try:
                tmp = float(line)
#Values are limited 300-2250 for safety
                if (tmp > 2250 or tmp < 300):
                    syslog.syslog("Incorrect clock value provided, setting default 1750")
                    tmp = 1750
                cclocks.append(tmp)
                print(tmp)
            except Exception as ex:
                print(ex)
        print(cclocks)
    try:
        test = subprocess.check_output("/opt/mine/gtool/ohgodatool -i 0 --show-mem", shell=True)
    except Exception as ex:
        igpu = 1
    for i, val in enumerate(cclocks):
        time.sleep(3)
        param = "/opt/mine/gtool/ohgodatool -i " + str(i + igpu) + " --mem-state 1" + " --mem-clock " + str(val)
        output = subprocess.call(param, shell=True)
        if output <> 0:
            syslog.syslog("Error: overclocking with GPU" + str(i + igpu))

#Array for core voltages
    cvoltages = []
#cvolt.conf for memory clock settings
    with open('cvolt.conf', 'r') as conf:
        data = conf.read()
        for line in data.split('\n'):
            try:
                tmp = float(line)
#Values are limited 800-1150 for safety
                if (tmp > 1150 or tmp < 800):
                    syslog.syslog("Incorrect clock value provided, setting default 1750")
                    tmp = 1150
                cvoltages.append(tmp)
                print(tmp)
            except Exception as ex:
                print(ex)
        print(cvoltages)
        
        for i, val in enumerate(cvoltages):
            time.sleep(3)
            for t in  range(1, 15):
                param = "/opt/mine/gtool/ohgodatool -i " + str(i + igpu) + " --volt-state " + str(t) +  " --vddc-table-set  " + str(val)
                output = subprocess.call(param, shell=True)
                if output <> 0:
                    syslog.syslog("Error: overclocking with GPU" + str(i + igpu))
