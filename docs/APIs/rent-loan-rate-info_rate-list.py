# 데이터명 : 한국주택금융공사_전세자금대출 금리 정보
# from : https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests

# url = https://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list?serviceKey=&pageNo=1&numOfRows=10&dataType=JSON   # http's'가 들어가면 error
url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'

# serviceKey=&wnv1AZgzQFIwUkVk8jaEll6P%2F89YW%2Bsft7aQQXNYv1WLsP8xAuc%2FnMAy9YAJu7MGgqYtTYOuyqCXl5YKKeVQAg%3D%3D
# &pageNo=1      
# &numOfRows=10
# &dataType=JSON
params = {'serviceKey' : '&wnv1AZgzQFIwUkVk8jaEll6P%2F89YW%2Bsft7aQQXNYv1WLsP8xAuc%2FnMAy9YAJu7MGgqYtTYOuyqCXl5YKKeVQAg%3D%3D'
          ,'pageNo' : 1
          ,'numOfRows' : 10
          ,'dataType' : 'JSON' }   # dict 선언

response = requests.get(url, params=params)    # response : class , get : 가져온다, params : dict으로 가져온다

print(response.content)

pass