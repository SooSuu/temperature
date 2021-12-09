import time
import schedule
import sqlite3
import Adafruit_DHT
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import logging
import pandas as pd
from pandas import DataFrame as df
import csv
import os
from datetime import date
dbname='sensorsData.db'  #데이터베이스랑 연결
sampleFreq = 30
now=datetime.datetime.now()  #현재 시간
today=now.strftime("%Y-%m") #문서를 만들때 써먹기 위한 년도와 달을 뺴오기
#hum, temp = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)
# 온도를 얻기위한 함수
def getDHTdata():            
    DHT22Sensor= Adafruit_DHT.DHT22
    DHTpin = 16
    hum,temp = Adafruit_DHT.read_retry(DHT22Sensor,DHTpin)
    if hum is not None and temp is not None:
        hum = round(hum)
        temp = round(temp, 1)
        return temp, hum
# 데이터를 저장하기 위한 함수
def logData (temp,hum):
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	curs.execute("INSERT INTO DHT_data values(datetime('now','localtime'), (?), (?))", (temp, hum))
	conn.commit()
	conn.close()
#문서를 저장하기 위한 함수
def cvscreate():
    xx=[] # 리스트를 만든 이유는 포문을 돌려서 리스트에 한줄씩 추가해주기 위해서
    yy=[]
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    for row in curs.execute("SELECT timestamp FROM DHT_data"):
        xx.append(row[0])
    for row in curs.execute("SELECT temp FROM DHT_data"):
        yy.append(row[0])

    df=pd.DataFrame(list(zip(xx,yy)),columns=('time','temp'))#데이터 프레임을 만들어 주기
    if not os.path.isdir(today): #위에서 선언한 년도와 달일 중첩되지않을때 만들어준다 
        os.makedirs(today)
    filename=datetime.datetime.now().strftime("%Y-%m-%d") #파일이름을  설장해주기
    df.to_csv(today+'/'+filename+'.cvs') # df=데이터프레임으로 csv파일을 만들고 파일경로 설정해주기 
    curs.execute("DELETE FROM DHT_data") # 다음날의 데이터를 위해서 초기화 시키는 예제
    conn.commit()
    conn.close()

def template(maxi,mini): #최대온도와 최소온도값을  받아온다
    temp,hum=getDHTdata() #현재 온도의값을 받아온다
    logData(temp,hum)    # 현재 온도의값을 저장해준다
    print("온도는= {0:0.1f}*C 습도는 = {1:0.1f}%".format(temp, hum)) #현재온도를 출력해준다
    if(temp>maxi or temp<mini):  # 현재온다가 최고온도보다 높거나 최저온도보다 낮을때 
        print("oh my god")
    
def main():
    print("최대온도를 설정 해 주세요")  
    maxi=float(input())   #최대 온도 값을 저장해준다 float로 설정해준이유는 그냥 input만 했을때에는 str 형식으로 저장되기 때문에
    print("최소온도를 설정 해 주세요")
    mini=float(input())
    temp,hum=getDHTdata() 
    logData(temp,hum)
    print("온도는= {0:0.1f}*C 습도는 = {1:0.1f}%".format(temp, hum)) #첨에 출력해주는 이유는 1분마다 루프가 돌아가기때문에 시작 온도를 체크해줄려고

    schedule.every().minute.at(":00").do(template,maxi,mini) # 00초마다 출력하게 만든다 00초마다 출력하는이유는 1분마다 출력 하게 해줄려고
    schedule.every().day.at("00:00").do(cvscreate) # 특정시간에 문서파일을 만들게 해줄려는 코드
    while True:
        schedule.run_pending()
        time.sleep(0.01)
main()
