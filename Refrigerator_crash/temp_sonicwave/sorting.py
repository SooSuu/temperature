'''
파일을 이동시키는 패키지를 불러온다
시간관련 패키지를 불러온다
os관련 패키지를 불러오는데, 일단 여기서는 폴더를 비교하는 명령어만 쓴다
'''
import shutil
import time
import os

# 현재 년-월-일을 설정하여 변수에다 저장하는 클래스를 gettoday()라고 부르기로 했어요
def gettoday():
    global day
    now = time.localtime()
    day = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
    return day

# 지금 년-월을 설정하여 변수에다 저장하는 클래스를 gettomonth()라고 부르기로 했어
def gettomonth():
    global month
    now = time.localtime()
    month = "%04d-%02d" % (now.tm_year, now.tm_mon)
    return month

# 폴더를 만드는 클래스, 그런데 폴더이름이 같으면 만들지 않음
def makefolder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

# 월 폴더의 이름을 정하는 클래스
def foldername_month():
    root_dir = "./video/"
    nowmonth = gettomonth()
    work_dir = root_dir + "/" + nowmonth
    
    makefolder(work_dir)

# 월 폴더 하위에 일 폴더의 이름을 정하는 클래스
def foldername_day():
    root_dir = "./video/" + gettomonth()
    today = gettoday()
    work_dir = root_dir + "/" + today
    
    makefolder(work_dir)

# 
def So():
    filename = 'camera.h264'
    dayfilename = (time.strftime("%Y-%m-%d_%Hh%Mm%Ss") + ".h264")
    src = "./"
    monthdir = "./video/" + month + "/"
    shutil.move(src + filename ,monthdir + dayfilename)
    daydir = "./video/" + month + "/" + day + "/"
    shutil.move(monthdir + dayfilename ,daydir + dayfilename)

if __name__ == '__main__':
    gettoday()
    foldername_day()
    So()
