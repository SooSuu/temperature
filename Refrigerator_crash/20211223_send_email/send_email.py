import os
import smtplib
import sqlite3
import datetime

from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_addr = formataddr(('온습도 관리 위원회', 'rkfaorl1480@gmail.com'))
to_addr = formataddr(('습온도 관리 위원회', 'rkfaorl1480@gmail.com'))
session = None


def getDaysBefore(day):
    dList = day.split("-")
    year = int(dList[0])
    month = int(dList[1])
    day = int(dList[2])
    
    d_day = datetime.datetime(year, month, day)
    now = datetime.datetime.now()
    
    return str(d_day - now).split("days")[0]


def logData():
    con=sqlite3.connect('/home/pi/Desktop/sensorsData.db')
    curs=con.cursor()
    now = datetime.datetime.now()
    
    for row in curs.execute('SELECT * FROM VACCINE ORDER BY EXPIRATION_DATE ASC LIMIT 1'):
        global time,name
        time = row[3]
        name = row[2]
        expiration = datetime.datetime.strptime(time,'%Y-%m-%d')
        con.commit()
        res = str(expiration - now).split("days")[0]
        res = int(res)

        if res < 0:
            while True:
                curs=con.cursor()
                curs.execute('DELETE FROM VACCINE ORDER BY EXPIRATION_DATE ASC LIMIT 1')
                con.commit()
                        
                for row in curs.execute('SELECT * FROM VACCINE ORDER BY EXPIRATION_DATE ASC LIMIT 1'):
                    time = row[3]
                    name = row[2]
                    expiration = datetime.datetime.strptime(time,'%Y-%m-%d')
                    con.commit()
                    res = str(expiration - now).split("days")[0]
                    res = int(res)
                    
                if res >= 0:
                    break
    con.close()
    return time, name


def Send_mail():
    try:
        # SMTP 세션 생성
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.set_debuglevel(True)
        
        # SMTP 계정 인증 설정회
        session.ehlo()
        session.starttls()
        session.login('rkfaorl1480@gmail.com', 'gaeq ocqv tfvr gqmx')
     
        # 메일 콘텐츠 설정
        message = MIMEMultipart("alternative")
        
        # 메일 송/수신 옵션 설정
        message.set_charset('utf-8')
        message['From'] = from_addr
        message['To'] = to_addr
        message['Subject'] = '비상비상'
     
        # 메일 콘텐츠 - 내용
        body = '''
        <h2>족됨</h2>
        <h4>온도 떨어진다~~~~</h4>
        <BODY>
        <IMG SRC="https://c.tenor.com/zCv6eiCrAKEAAAAC/tom-and-jerry-flee.gif">
        </BODY>
        '''
        bodyPart = MIMEText(body, 'html', 'utf-8')
        message.attach( bodyPart )
        
        # 메일 발송
        session.sendmail(from_addr, to_addr, message.as_string())            
     
        print( 'Successfully sent the mail!!!' )
    except Exception as e:
        print( e )
    finally:
        if session is not None:
            session.quit()

target_time, vaccine_name = logData()
D_Day = getDaysBefore(target_time)
D_Day_int = int(D_Day)

if D_Day_int <= 7  and D_Day_int >= 0:
    Send_mail()
