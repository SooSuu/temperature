from time import sleep
import time
import sqlite3 as sql
from w1thermsensor import W1ThermSensor
import send_email

sensor = W1ThermSensor()

def tem():
    temperature = sensor.get_temperature()
    return temperature

def get_temperature_setting_value():
    con=sql.connect('/home/pi/Desktop/alarm_email/sensorsData.db')
    curs=con.cursor()
    for row in curs.execute('SELECT * FROM TEMP_R ORDER BY CREATED_AT DESC LIMIT 1'):
        now_max = row[2]
        now_min = row[3]
        
    con.close()
    
    return now_max, now_min

# This function checks the threshold temperature and lights up an led
try:
    while True:
        Temp = tem()
        now_max, now_min = get_temperature_setting_value()
        print('nowTemp : ' + str(Temp))
        print('MAX : ' + str(now_max),'MIN : ' + str(now_min))
        
        if Temp < now_min or Temp > now_max:
            send_email.Send_mail()
        else:
            pass

        time.sleep(60)
        
except KeyboardInterrupt:
    print("***end***")
        
