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
#conn=sqlite3.connect('sensorsData.db')
#curs=conn.cursor()
dbname='sensorsData.db'
conn=sqlite3.connect(dbname)
curs=conn.cursor()
data=[]
xx=[]
result=[]
named=[]
date_time_obj=[]
rows=[]
cc=[]
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
    ma= time + relativedelta(years=2)
    dangers= time2 + relativedelta(days=3)
    print("백신의 이름명을 입력해 주세요")
    name=input()
    print("유통기한이 몇일 인가요 ?")
    PlusDays=int(input())
    shelf=time2+timedelta(days=PlusDays)
    logData(name,shelf)
    for row in curs.execute("SELECT strftime('%Y-%m-%d',timestamp) from shelf_life"):
        data.append(row[0])
    for ro in curs.execute("SELECT name from shelf_life"):
        named.append(ro[0])
    curs.execute("SELECT row_number() over(order by name asc) as number,name,shelf from shelf_life ")
    for row in curs.fetchall():
        date_time_str=row[2]
        date_time_obj=datetime.strptime(date_time_str,'%Y-%m-%d %H:%M:%S')
        curs.execute("SELECT ROW_NUMBER() OVER(ORDER BY shelf)AS row FROM shelf_life")
        if date_time_obj>time2:
            result.append(date_time_obj)
            curs.execute("INSERT INTO Shelf_made(name,shelf) SELECT name,shelf FROM shelf_life ")
            curs.execute("DELETE FROM shelf_life where shelf < "time2" ")
    for row in curs.execute("SELECT * from shelf_made"):
        cc.append(row[1])
        xx.append(row[2])
    print(cc)
    print(xx)
    print(result)
    print(named)
    plt.axis([0,30,time,ma])
    plt.bar(named,result)
    plt.show()
    
main()
