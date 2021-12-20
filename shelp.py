import time
from datetime import date
import sqlite3
import pandas as pd
from pandas import DataFrame as df
import schedule
from datetime import date,datetime,timedelta
from matplotlib import dates
import plotly.express as px
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
import matplotlib.font_manager 
import matplotlib as mpl
#conn=sqlite3.connect('sensorsData.db')
#curs=conn.cursor()
dbname='sensorsData.db'
conn=sqlite3.connect(dbname)
curs=conn.cursor()
result=[]
named=[]
date_time_obj=[]
rows=[]
postshelf=[]
postnamed=[]
def logData(name,shelf):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO Shelf_life values(date('now','localtime'),(?),(?))",(name,shelf))
    conn.commit()
    conn.close()
def main():
    time = datetime.now()
    time1 = time.strftime('%Y-%m-%d %H:%M:%S')
    time2 = datetime.strptime(time1,'%Y-%m-%d %H:%M:%S')
    dangers= time2 + relativedelta(days=3)
    print("백신의 이름명을 입력해 주세요")
    name=input()
    print("유통기한이 몇일 인가요 ?")
    PlusDays=int(input())
    print("몇일뒤 그래프까지 보고 싶으세요?")
    PlusMonth=int(input())
    shelf=time2+timedelta(days=PlusDays)
    ma= time + relativedelta(days=PlusMonth)
    logData(name,shelf)
    curs.execute("SELECT * from shelf_life")
    
    for row in curs.fetchall():
        date_time_str=row[2]
        date_time_obj=datetime.strptime(date_time_str,'%Y-%m-%d %H:%M:%S')
        if date_time_obj>time2:
            result.append(date_time_obj)
            named.append(row[1])
        else:
            postnamed.append(date_time_obj)
            postshelf.append(row[1])
    
    mpl.rcParams['axes.unicode_minus'] = False
    plt.rcParams["font.family"] = 'NanumGothic'
    plt.axis([0,30,time,ma])
    plt.xlabel('Vaccine name')
    plt.ylabel('Expiration days')
    plt.bar(named,result)
    plt.show()
    
main()
