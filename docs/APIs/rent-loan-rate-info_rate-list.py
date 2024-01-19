## 데이터명 : 한국주택금융공사_전세자금대출 금리 정보
# from : https://www.data.go.kr/iim/api/selectAPIAcountView.do   # 마이페이지 - 데이터활용 - Open API - 활용신청 현황 - 해당 클릭 - 개발계정 상세보기
import requests

# url = https://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list?serviceKey=&pageNo=1&numOfRows=10&dataType=JSON   # http's'가 들어가면 error
url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'

# serviceKey=&wnv1AZgzQFIwUkVk8jaEll6P%2F89YW%2Bsft7aQQXNYv1WLsP8xAuc%2FnMAy9YAJu7MGgqYtTYOuyqCXl5YKKeVQAg%3D%3D
# &pageNo=1      
# &numOfRows=10
# &dataType=JSON
params = {'serviceKey' : 'wnv1AZgzQFIwUkVk8jaEll6P/89YW+sft7aQQXNYv1WLsP8xAuc/nMAy9YAJu7MGgqYtTYOuyqCXl5YKKeVQAg=='   # Encoding(%3D%3D)이 아닌 Decoding(==) 일반 인증키 값 가져오기
          ,'pageNo' : 1
          ,'numOfRows' : 10
          ,'dataType' : 'JSON'}   # dict 선언

response = requests.get(url, params=params)    # response : class , get : 가져온다, params : dict으로 가져온다

print(response.content)

import json
contents = json.loads(response.content)

## DEBUG CONSOLE
type(contents)
# <class 'dict'>
contents['header']
# {'resultCode': '00', 'resultMsg': '정상'}
contents['header']['resultCode']
# '00'
contents['body']['totalCount']
# 18
type(contents['body']['items'])     # list 정보
# <class 'list'>

## mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["data_go_kr"]  # data_go_kr : 정부데이터

# collection 작업
collection = database['rent-loan-rate-info_rate-list']  # collection : 파일명 : rent-loan-rate-info_rate-list

# insert 작업 진행
result = collection.insert_many(contents['body']['items'])
pass