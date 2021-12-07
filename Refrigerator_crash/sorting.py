'''
파일을 이동시키는 패키지를 불러온다
시간관련 패키지를 불러온다
os관련 패키지를 불러오는데, 일단 여기서는 폴더를 비교하는 명령어만 쓴다
'''
import shutil
import time
import os

# 폴더를 만드는 함수, 그런데 폴더이름이 같으면 만들지 않음
def makefolder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)


# 지금 년-월을 설정하여 변수에다 저장하는 함수를 gettomonth()라고 부르기로 했어요
# global month는 So() 함수에서 쓸거라서 전역변수로 지정한거임
def gettomonth():
    global month
    now = time.localtime()
    month = "%04d-%02d" % (now.tm_year, now.tm_mon)
    return month


# 현재 년-월-일을 설정하여 변수에다 저장하는 함수를 gettoday()라고 부르기로 했어요
# global day는 So() 함수에서 쓸거라서 전역변수로 지정한거임
def gettoday():
    global day
    now = time.localtime()
    day = "%04d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
    return day


# '월' 폴더의 이름을 정하는 함수
def foldername_month():
    root_dir = "./video/"
    nowmonth = gettomonth()
    work_dir = root_dir + "/" + nowmonth
    
    makefolder(work_dir)


# 월 폴더 하위에 '일' 폴더의 이름을 정하는 함수
def foldername_day():
    root_dir = "./video/" + gettomonth()
    today = gettoday()
    work_dir = root_dir + "/" + today
    
    makefolder(work_dir)


# ./video/월별/일별로 폴더를 만들어서 비디오를 저장하려는 의도를 가진 함수 ['So'rting]
# 동영상이 최초로 녹화가 되면 루트 디렉토리에[파이썬 코드가 있는 디렉토리에] camera.h264 파일이 저장이 된다
# camera.h264를 현재 년-월-일-시간으로 설정된 제목으로 변경하여, dayfilename 이라는 변수에다 저장한다
# 월,일로 생성된 폴더안에 파일을 넣겠다는 코드[shutil.move]
# 결론) 그러니까 video 폴더가 있어야 한다고
def So():
    filename = 'camera.h264'
    dayfilename = (time.strftime("%Y-%m-%d_%Hh%Mm%Ss") + ".h264")
    src = "./"
    monthdir = "./video/" + month + "/"
    shutil.move(src + filename ,monthdir + dayfilename)
    daydir = "./video/" + month + "/" + day + "/"
    shutil.move(monthdir + dayfilename ,daydir + dayfilename)


# 오늘 날짜를 설정하고
if __name__ == '__main__':
    gettomonth()
    gettoday()
    foldername_month()
    foldername_day()
    So()
