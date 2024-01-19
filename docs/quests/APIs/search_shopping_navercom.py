# from : https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md#%EC%87%BC%ED%95%91

import requests     # postman app 역할

#  request API에 요청 부분
url = "https://openapi.naver.com/v1/search/shop"
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
pass

## mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["developers_naver"]  # 폴더
# collection 작업
collection = database['search_shop_info']  # 파일
collection = database['search_shop_list']  # 파일 search_shop_list(id_relative)
# insert 작업 진행
# result = collection.insert_many(contents['body']['items'])

pass