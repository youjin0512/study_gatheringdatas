# * quests
# docs/quests/watcha_comments_pagescrolls_selectors.py
# - refer : watcha_pagescrolls_selectors.py
# - 각 댓글 mongo(db명 : gatheringdatas, collection명 : watcha_comments)DB에 저장
# - 댓글 : 작성자, 별점 점수, 내용

## 필요한 라이브러리 임포트
# * 웹 크롤링 동작      # 셀레니움에서 웹드라이버 임포트
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

webdriver_manager_directory = ChromeDriverManager().install()

#chrome browser 열기
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
browser.get("https://pedia.watcha.com/ko-KR/contents/mDWvXDd/comments") # 웨스트 사이드 스토리 comments

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# 한 페이지씩 이동
element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")   # element_body이 scroll되서 정보가 들어감


def connect_mongo() : 
    # mongodb compass 띄우기
    from pymongo import MongoClient     # pymongo : module, Mongoclient : class      # client : mongoDB의 compass 같은 역할
    # mongodb에 접속(connection) -> 자원에 대한 class
    mongoClient = MongoClient("mongodb://192.168.10.184:27017/")   # mongoClient : class를 담은 변수  # 내 주소
    # database 연결
    database = mongoClient["gatheringdatas"]
    # collection 작업
    collection = database['watcha_comments']
    return collection




## 여러개(복수) elements 정보 가져오기  <-- 어떤 find를 했을 때 정보가 여러 개 라는 의미
selector_value = "div.info"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)   # value : 전체

elements_path = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)  # find_element's' 추가 / elements_path에도 's' 추가
type(elements_path)




previous_scrollHeight = 0
while True : 
    element_body.send_keys(Keys.END)
    current_scrollHeight = browser.execute_script("return document.body.scrollHeight")    # execute_script : chrome console에서 동작시키기 위함
    if previous_scrollHeight >= current_scrollHeight :     # previous가 current보다 크거나 같을 때 break
        break
    else :
         previous_scrollHeight = current_scrollHeight      # currnet를 previous라는 변수에 값 할당
    time.sleep(2)  # sleep 속도 2
    list_count_comments = browser.find_elements(by=By.CSS_SELECTOR, value="div > ul > div.css-13j4ly.egj9y8a4")

for count_comments in range(len(list_count_comments)) : # comments 개수 만금 for문 돌리기
    try :  # writer(작성자)
        element_writer = browser.find_element(by=By.CSS_SELECTOR, value="div.css-eldyae.e10cf2lr1")    # value : element 접근자
        writer = element_writer.text
        pass    # 정식 코드
    except :
        writer = ""     # 특정 항목에서는 태그가 없을 수 있다
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass    # try나 except이 끝난 후 무조건 실행 코드

    try :  # rate(평점)
        element_rate = browser.find_element(by=By.CSS_SELECTOR, value="div.css-31ods0.egj9y8a0")
        rate = element_rate.text
        pass    
    except :
        rate = ""
        pass
    finally :
        pass

    try :  # contents(내용)
        element_contents = browser.find_element(by=By.CSS_SELECTOR, value="div.css-10w4kfx.e1hvy88212")
        contents = element_contents.text
        pass    
    except :
        contents = ""
        pass
    finally :
        pass


    col_watcha = connect_mongo()
    col_watcha.insert_one({"writer":writer, "rate":rate, "contents":contents})
    pass

browser.find_elements(by=By.CSS_SELECTOR, value="")


data = {
    'writer': '작성자',
    'rate': '평점',
    'contents': '내용'
}


col_watcha.insert_one(data)

# 브라우저 종료
browser.quit()