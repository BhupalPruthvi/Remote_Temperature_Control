# Remote_Temperature_Control

import smtplib
import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

#CELSIUS CALCULATION
def read_temp_c():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = int(temp_string) / 1000.0 # TEMP_STRING IS THE SENSOR OUTPUT, MAKE SURE IT'S AN INTEGER TO DO THE MATH
        temp_c1 = str(round(temp_c, 1)) # ROUND THE RESULT TO 1 PLACE AFTER THE DECIMAL, THEN CONVERT IT TO A STRING
        if temp_c1<20:
            print 'Temp <20'
			
        else :
            for i in range(1):
                for j in range(2):
                    smtpUser = 'joseph.adidhala.717@my.csun.edu'
                    smtpPass = 'Victor123$$'
                    toAdd = 'joseph.adidhala@gmail.com'
                    fromAdd = smtpUser
                    print 'To: '
                    print toAdd
                    print 'From: '
                    print fromAdd
                    print 'Subject: '
                    subject='Temperature at AMIC burbank is'
                    print subject
                    body = temp_c1
                    print body
                    temp_x=temp_c1
                    s = smtplib.SMTP('smtp.gmail.com',587)
                    s.ehlo()
                    s.starttls()
                    s.ehlo()
                    s.login(smtpUser, smtpPass)
                    s.sendmail(fromAdd, toAdd, subject+body+temp_x)
                    s.quit () 
                    print 'Temp greater'
                    time.sleep(120)
                time.sleep(900)
		return temp_c1
        
    
    

#FAHRENHEIT CALCULATION
def read_temp_f():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_f = (int(temp_string) / 1000.0) * 9.0 / 5.0 + 32.0 # TEMP_STRING IS THE SENSOR OUTPUT, MAKE SURE IT'S AN INTEGER TO DO THE MATH
        temp_f = str(round(temp_f, 1)) # ROUND THE RESULT TO 1 PLACE AFTER THE DECIMAL, THEN CONVERT IT TO A STRING
        print temp_f
        return temp_f

    


while True:
   read_temp_c()
   read_temp_f()






   
   

