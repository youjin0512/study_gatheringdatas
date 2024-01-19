# from : https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4

import requests     # postman app 역할

#  request API에 요청 부분
url = "https://openapi.naver.com/v1/search/news"
params = {'query' : '인공지능'}  # dictionary
headers = {'X-Naver-Client-Id' : 'qIBjwLF8Ab4sHsQ48qto'    # 애플리케이션 등록 시 발급받은 클라이언트 아이디 값
           ,'X-Naver-Client-Secret' : '9D3KZbF4Ah'}        # 애플리케이션 등록 시 발급받은 클라이언트 시크릿 값
response =  requests.get(url, params=params, headers=headers)

# response API에 응답 부분
response.content

# json을 변수로 변환
import json
contents = json.loads(response.content)
type(contents)
# <class 'dict'>
type(contents['total'])
# <class 'int'>
pass