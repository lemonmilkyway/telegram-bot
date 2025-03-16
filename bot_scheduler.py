import logging
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# 🔥 디버깅 로그 활성화
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# 🚀 BotFather에서 받은 토큰 입력
TOKEN = "7652647611:AAG011W5j6UPxfOXAse0IptLT5HwsqxjRKA"  # 🔥 여기에 봇 토큰 입력
GROUP_ID = -1002341269765  # 🔥 그룹 ID 입력
THREAD_ID = 5  # 🔥 특정 토픽 ID 입력

# 🔹 자동 메시지 전송 함수
def send_scheduled_message():
    today = datetime.today().strftime("%m월/%d일")  # 날짜 포맷 (03월/16일)
    message = f"""
🔰2팀 6구역 전도 일일보고 ({today})
     🔥 일보마감22시 🔥

1️⃣ 전도활동
1. 오프라인(대면) 활동자 명단 :
2. 온라인 활동자 명단 : 

3. 번호찾기
  (팀/구역/섭/인/섭외경로(&도구)/나이/성별/사는곳/번호/만픽여부⭕️❌)
-

4. 합자찾기 
  (팀/구역/섭/인/섭외경로(도구)/합찾양식링크)
- 

5. 만남 : 인도자가 보고
  (팀/구역/섭/인/교/총0회만남)
- 
6. 신규육따 : 인도자가 보고
  (팀/구역/섭/인/교/주0회)
- 
7. 신규성따 : 교사가 보고
  (팀/구역/섭/인/교/주0회)
- 
8. 복음방진행 : 교사가 보고
  (팀/구역/섭/인/교/총0회차/제목)
-
9. 오픈
  (팀/구역/섭/인/교/오픈자)
-

2️⃣ 기타활동
(1) 총회장님글 배포
     (팀/구역/이름/배포수/교회or개인)
-
(2) 국내섬김이 (센터/기수/수강생/섬김이)
- 
(3) 잎사귀 (섭/인/잎/내용) (&인교의 섬김)
-
(4) 인스타DM 발송 수
      (팀/구역/이름/도구/발송 수)
- 
    """

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": GROUP_ID,
        "message_thread_id": THREAD_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=data)
        logging.info(f"✅ 메시지 전송 완료: {response.json()}")
    except Exception as e:
        logging.error(f"🚨 메시지 전송 실패: {e}")

# 🕕 매일 18시에 자동 메시지 전송 설정
scheduler = BlockingScheduler()
scheduler.add_job(send_scheduled_message, "cron", hour=18, minute=0)

# ✅ 즉시 테스트 메시지 보내기 (코드 실행 시 바로 한 번 전송됨)
send_scheduled_message()

# 🕘 스케줄러 실행 (계속 실행됨)
scheduler.start()
