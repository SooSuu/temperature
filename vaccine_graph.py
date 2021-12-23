import time
import sqlite3
from datetime import date,datetime,timedelta
from matplotlib import dates
from matplotlib import dates
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.font_manager
import matplotlib as mpl
from dateutil.relativedelta import relativedelta

def graph():
    result=[]
    named=[]
    postshelf=[]
    postnamed=[]
    time = datetime.now()
    time1 = time.strftime("%Y-%m-%d %H:%M:%S")
    time2 = datetime.strptime(time1,"%Y-%m-%d %H:%M:%S")
    ymax=time2+relativedelta(days=30)
    conn=sqlite3.connect('../sensorsData.db')
    curs=conn.cursor()
    curs.execute("SELECT * from VACCINE")
    for row in curs.fetchall():
        date_time_str=row[3]
        date_time_obj=datetime.strptime(date_time_str,'%Y-%m-%d')
        if date_time_obj>time:
            result.append(date_time_obj)
            named.append(row[2])
        else:
            postnamed.append(date_time_obj)
            postshelf.append(row[2])
    print(result)
    mpl.rcParams['axes.unicode_minus'] = False
    plt.rcParams["font.family"]='NanumGothic'
    plt.axis([0,30,time,ymax])
    plt.title("백신")
    plt.xlabel('Vaccine name')
    plt.ylabel('days')
    plt.bar(named,result,label='유통기한')
    plt.legend()

    # 그래프 저장 경로
    plt.savefig('/home/pi/777/dhtWebServer/static/vaccine.png')
    plt.show()
    
graph()
