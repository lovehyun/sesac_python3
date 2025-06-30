# pip install requests
# pip uninstall requests

# 더이상 빌트인 모듈이 아니고, 외부 라이브러리르 설치하는것..
# 외부는 어디냐??
# https://pypi.org/
# 이게 어디에서 설치???
# 나의 파이썬 가상환경 내의 라이브러리 공간에 설치됨

import requests

response = requests.get("http://makemyproject.net")
print(response)
print(response.status_code)
print(response.text)

