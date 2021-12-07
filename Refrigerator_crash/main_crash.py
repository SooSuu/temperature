'''
camera.py 파일을 불러온다
crash.py 파일을 불러온다
sorting.py 파일을 불러온다
시간 관련 패키지를 불러온다
'''
import camera
import crash
import sorting
import time

# 3초간 '지속적으로' 물체가 감지되었을때를 판별하기 위한 변수
flag = 0

try:
	while True:
        # 충돌 센서를 이용한 충돌감지 함수 crash_check()를 crash.py 에서 불러온다
		result = crash.crash_check()
		if result == 1:
			print("진동이 감지 되었습니다.")
		else:
			print("진동이 없습니다.")

        # 입력값이 1일때[충돌이 감지되었을 때] flag 변수를 1씩 증가시키고, 그렇지 않을때 flag 를 초기화 시킨다
        # 플래그는 충돌감지의 민감도를 설정하는 맥락으로 코드를 짜 보았다
		if result == 1:
			flag += 1
		else:
			flag = 0

      	 	# camera.py 의 Rec() [녹화] , sorting 의 gettoday()/foldername()/So() 
		# [대충 날짜대로 폴더 만들고 폴더안에 날짜적힌 동영상 파일이 저장되는 클래스]
		if flag >= 3:
			camera.Rec()
			sorting.gettomonth()
			sorting.gettoday()
			sorting.foldername_month()
			sorting.foldername_day()
			sorting.So()
			flag = 0

       	 	# 1초간 딜레이를 준다 = while문이 한바퀴 도는 시간이 대략 1초가 된다
		time.sleep(1)

# 파이썬 가동 중에 ctrl + c 를 누르면 멈추면서 나타나는 문구
except KeyboardInterrupt:
	print("Measurement stopped by User")
	GPIO.cleanup()
        
        
