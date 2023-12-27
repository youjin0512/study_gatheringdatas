# * 웹 크롤링 동작      # 셀레니움에서 웹드라이버 임포트
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
browser.get("https://www.11st.co.kr/products/pa/6406642119?inpu=&trTypeCd=22&trCtgrNo=895019")   # 11번가 덴티스테

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# iframe으로 전환
browser.switch_to.frame('ifrmReview')

# 한 페이지씩 이동
element_body = browser.find_elements(by=By.CSS_SELECTOR, value="#review-list-area")
time.sleep(3)

while True :
    try :
        # browser.find_element(by=By.CSS_SELECTOR, value="menuLink84").click()   # 아래 2줄과 동일한 내용
        element_click = browser.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > div > button")  # 메뉴 더보기 버튼
        click_button = element_click.click()
        time.sleep(5)
    except :
        break



def connect_mongo() : 
    # mongodb compass 띄우기
    from pymongo import MongoClient     # pymongo : module, Mongoclient : class      # client : mongoDB의 compass 같은 역할
    # mongodb에 접속(connection) -> 자원에 대한 class
    mongoClient = MongoClient("mongodb://192.168.10.184:27017/")   # mongoClient : class를 담은 변수  # 내 주소
    # database 연결
    database = mongoClient["gatheringdatas"]
    # collection 작업
    collection = database['11st_comments']
    return collection



## 여러개(복수) elements 정보 가져오기  <-- 어떤 find를 했을 때 정보가 여러 개 라는 의미
selector_value = "li.review_list_element"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)   # value : 전체



for count_comments in element_bundle : # comments 개수 만금 for문 돌리기
    try :  # writer(작성자)
        element_writer = count_comments.find_element(by=By.CSS_SELECTOR, value="dt.name")    # value : element 접근자
        writer = element_writer.text
        pass
    except :
        writer = ""
        pass
    finally :
        pass

    try :  # option(선택옵션)
        element_option = count_comments.find_element(by=By.CSS_SELECTOR, value="div > dl > div")
        option = element_option.text
        pass    
    except :
        rate = ""
        pass
    finally :
        pass

    try :  # rate(별점)
        element_rate = count_comments.find_element(by=By.CSS_SELECTOR, value="div > p.grade > span")
        rate = element_rate.text
        pass    
    except :
        rate = ""
        pass
    finally :
        pass

    try :  # contents(내용)
        element_contents = count_comments.find_element(by=By.CSS_SELECTOR, value="div > div > div.cont_text_wrap > p")
        contents = element_contents.text
        pass    
    except :
        contents = ""
        pass
    finally :
        pass

    col_11st = connect_mongo()
    col_11st.insert_one({"writer":writer, "option":option, "rate":rate, "contents":contents})
    pass



# 브라우저 종료
browser.quit()