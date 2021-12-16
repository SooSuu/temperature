import matplotlib.pyplot as plt
import numpy as np
from matplotlib import dates
import sqlite3
import os
import pandas as pd
from pandas import DataFrame as df
from matplotlib.ticker import MultipleLocator, IndexLocator, FuncFormatter
from matplotlib.dates import MonthLocator, DateFormatter
import matplotlib.dates as mdates
import datetime
from datetime import date
import csv
conn=sqlite3.connect('sensorsData.db')
curs=conn.cursor()
curs.execute("SELECT strftime('%H:%M',timestamp) FROM DHT_data")
now=datetime.datetime.now()
today=now.strftime("%Y-%m")
xx=[]
for row in curs.fetchall():
    xx.append(row[0])
curs.execute("SELECT temp FROM DHT_data")
yy=[]
for row in curs.fetchall():
    yy.append(row[0])
curs.execute("SELECT hum FROM DHT_data")
zz=[]
for row in curs.fetchall():
    zz.append(row[0])

if not os.path.isdir(today):
    os.makedirs(today)
filename = datetime.datetime.now().strftime("%Y-%m-%d")
plt.savefig(today+'/'+filename+'.png')
fig=plt.figure()
ax=fig.add_subplot()
ax.tick_params(axis='x',width=3,which='major',length=5,color='b')
plt.plot(xx,yy,'r-',marker='o')
if not os.path.isdir(today):
    os.makedirs(today)
filename = datetime.datetime.now().strftime("%Y-%m-%d")
plt.savefig(today+'/'+filename+'.png')
plt.show()

#df=pd.DataFrame(list(zip(xx,yy,zz)),columns=('time','temp','hum'))
#img_path = current_app.root_path + '/static/img/receipts/' + datetime.datetime.now().strftime('%Y/%m/') 
#if not os.path.exists(img_path): 
#now=datetime.datetime.now()
#today=now.strftime("%Y-%m")
#if not os.path.isdir(today):
#    os.makedirs(today)
#filename = datetime.datetime.now().strftime("%Y-%m-%d")
#plt.savefig(today+'/'+filename+'.png')
#df=pd.DataFrame(list(zip(xx,yy,zz)),columns=('time','temp','hum'))
#df=pd.DataFrame(list(zip(xx,yy,zz)),columns=('time','temp','hum'))
#df=pd.DataFrame(list(zip(xx,yy,zz)),columns=('time','temp','hum'))
#img_path = current_app.root_path + '/static/img/receipts/' + datetime.datetime.now().strftime('%Y/%m/') 
#if not os.path.exists(img_path): 
#now=datetime.datetime.now()
#today=now.strftime("%Y-%m")
#if not os.path.isdir(today):
#    os.makedirs(today)
#filename = datetime.datetime.now().strftime("%Y-%m-%d")
#plt.savefig(today+'/'+filename+'.png')
