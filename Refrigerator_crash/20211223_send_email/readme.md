# 이메일 보내기

1. 디데이 7일일때 이메일 보냄

2. 기간이 다 된 DB값은 알아서 지움 **진짜 DB안에 값을 지움**

3. DB에서 입력받는 로그인 ID를 from_addr에 입력하는건 아직 **미구현**
   * 로그인이 선행기술

4. logData()함수 관련
   * 현재 sqlite3를 불러오는 링크를 '/home/pi/Desktop/sensorsData.db' 로 **절대경로**로 지정을 해놓음
   * 그것의 이유는 나중에 자동 실행을 위해서 crontab을 이용해서 실험해봤지만 왠지 모르게 './sensorsData.db'로 절대경로가 안먹힘 ㅎㅎ;;
   * 그래서 나중에 더 좋은 방안이 있으면 수정하거나, 나중에 시연할때는 조금 주의해서 코드를 수정하기
