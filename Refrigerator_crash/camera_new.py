'''
파이 카메라 관련 패키지를 불러온다
시간 관련 패키지 중에서 sleep 명령어만 사용한다는 뜻
'''
import os
from time import sleep


# '3'초간 녹화를 하겠다는 함수를 Rec()라고 부르기로 했어요
def Rec():
    # 대충 녹화 시작하고 3초 녹화하다 끝내고 camera.h264로 저장하겠다는 내용
    os.system ("libcamera-vid -o camera.h264")
    
    

if __name__ == '__main__':
    Rec()
