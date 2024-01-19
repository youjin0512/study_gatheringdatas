## 데이터명 : 기상청_관광코스별 관광지 상세 날씨 조회서비스
# from : https://www.data.go.kr/iim/api/selectAPIAcountView.do   # 마이페이지 - 데이터활용 - Open API - 활용신청 현황 - 해당 클릭 - 개발계정 상세보기

import requests

url = 'http://apis.data.go.kr/1360000/TourStnInfoService1/getCityTourClmIdx1'  # 상세설명서 docs 파일 다운로드 받아 서비스 URL 가져오기
# https://apis.data.go.kr/1360000/TourStnInfoService1/getCityTourClmIdx1?serviceKey=wnv1AZgzQFIwUkVk8jaEll6P%2F89YW%2Bsft7aQQXNYv1WLsP8xAuc%2FnMAy9YAJu7MGgqYtTYOuyqCXl5YKKeVQAg%3D%3D&pageNo=1&numOfRows=10&dataType=JSON&CURRENT_DATE=2018123110&DAY=3&CITY_AREA_ID=5013000000
# serviceKey=wnv1AZgzQFIwUkVk8jaEll6P%2F89YW%2Bsft7aQQXNYv1WLsP8xAuc%2FnMAy9YAJu7MGgqYtTYOuyqCXl5YKKeVQAg%3D%3D
# &pageNo=1
# &numOfRows=10
# &dataType=JSON
# &CURRENT_DATE=2018123110
# &DAY=3
# &CITY_AREA_ID=5013000000

params = {'serviceKey' : 'wnv1AZgzQFIwUkVk8jaEll6P/89YW+sft7aQQXNYv1WLsP8xAuc/nMAy9YAJu7MGgqYtTYOuyqCXl5YKKeVQAg=='   # Encoding(%3D%3D)이 아닌 Decoding(==) 일반 인증키 값 가져오기
          ,'pageNo' : 1
          ,'numOfRows' : 10
          ,'dataType' : 'JSON'
          ,'CURRENT_DATE' : 2018123110
          , 'DAY' : 3
          ,'CITY_AREA_ID' : 5013000000}   # dict 선언

response = requests.get(url, params=params)    # response : class , get : 가져온다, params : dict으로 가져온다

print(response.content)

import json
contents = json.loads(response.content)

## DEBUG CONSOLE
type(contents)
# <class 'dict'>
type(contents['response'])
# <class 'dict'>
type(contents['response']['body'])
# <class 'dict'>
type(contents['response']['body']['items'])
# <class 'dict'>
type(contents['response']['body']['items']['item'])
# <class 'list'>

## mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["data_go_kr"]  # data_go_kr : 정부데이터

# collection 작업
collection = database['TourStnInfoService1']  # collection : 파일명 : TourStnInfoService1

# insert 작업 진행
result = collection.insert_many(contents['response']['body']['items']['item'])
pass