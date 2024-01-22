# from : https://openapi.naver.com/v1/datalab/shopping/categories \

import requests     # postman app 역할

#  request API에 요청 부분
url = "https://openapi.naver.com/v1/datalab/shopping/categories"
headers = {'X-Naver-Client-Id' : 'lyeZsQLthDvwuAFBTYjP'    # 애플리케이션 등록 시 발급받은 클라이언트 아이디 값
           ,'X-Naver-Client-Secret' : 'jqdYaPCJiX'}        # 애플리케이션 등록 시 발급받은 클라이언트 시크릿 값
bodys = {
    "startDate": "2017-08-01",
    "endDate": "2017-09-30",
    "timeUnit": "month",
    "category": [
        {"name": "패션의류", "param": [ "50000000"]},
        {"name": "화장품/미용", "param": [ "50000002"]}
    ],
    "device": "pc",
    "gender": "f",
    "ages": [ "20",  "30"]
            }
response =  requests.post(url, headers=headers, json=bodys)

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