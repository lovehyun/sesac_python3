import urllib.request
import json

client_id = ""  # 여기에 발급받은 ID/Secret 을 입력
client_secret = ""

text = "Python 개발"

encText = urllib.parse.quote(text)
url = 'https://openapi.naver.com/v1/search/blog?query=' + encText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    print(response_body.decode('utf-8'))
