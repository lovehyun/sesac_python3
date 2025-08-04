import smtplib
from email.mime.text import MIMEText  # 메일의 컨텐츠 인코딩 포멧

import os
from dotenv import load_dotenv
load_dotenv()

SMTP_SERVER = 'smtp.naver.com'  # 이거도 사실 환경...
SMTP_PORT = 587  # SMTP 는 465, IAMP은 587 (그럼에도 서버 주소는 동일함)

NAVER_EMAIL = os.getenv("NAVER_EMAIL")
NAVER_PASSWORD = os.getenv("NAVER_PASSWORD")

# RECIPIENT_MAIL = '받는사람메일주소@메일서버.com'
RECIPIENT_MAIL = NAVER_EMAIL

# 메일 내용
subject = '네이버 이메일 테스트 입니다.'
body = '이 메일은 파이썬을 통해서 생성되었습니다.'

# 우리가 보내고 싶은 내용을 MIME 타입으로 인코딩
message = MIMEText(body, _charset='utf-8')
message['subject'] = subject
message['from'] = NAVER_EMAIL
message['to'] = RECIPIENT_MAIL

try:
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls() # TLS 보안 연결 시작
    smtp.login(NAVER_EMAIL, NAVER_PASSWORD) # 로그인
    smtp.sendmail(NAVER_EMAIL, RECIPIENT_MAIL, message.as_string()) # 전송
    print("메일이 성공적으로 발송 되었습니다.")
except Exception as e:
    print(f"메일 전송 중 오류 발생: {e}")
finally:
    smtp.quit() # 종료
