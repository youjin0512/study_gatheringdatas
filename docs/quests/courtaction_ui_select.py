# * quest
# - refer : seleniums/courtauction_ui_Select_selector.py
# - 대상 : https://www.courtauction.go.kr/
# - 물건상세검색 : 조건 (법원소재지 최소 3개)
# - 저장 사항 : 법원소재지, 사건번호, 소재지및내역 (몽고DB에담기)
#    db : gatheringdatas / collection : courtauction
# - option) select_by_index 적용 완료분은 select_by_value로 적용 고려

# * 웹 크롤링 동작      # 셀레니움에서 웹드라이버 임포트
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
browser.get("https://www.courtauction.go.kr/") # 대한민국 법원 경매정보

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
# refer official : https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select
from selenium.webdriver.support.ui import Select
# Select(driver.find_element(By.TAG_NAME, “select”)).select_by_index(2)  # driver.find_element(By.TAG_NAME, “select” : select에 있는 element(tag)

def connect_mongo() : 
    # mongodb compass 띄우기
    from pymongo import MongoClient     # pymongo : module, Mongoclient : class      # client : mongoDB의 compass 같은 역할
    # mongodb에 접속(connection) -> 자원에 대한 class
    mongoClient = MongoClient("mongodb://192.168.10.184:27017/")   # mongoClient : class를 담은 변수  # 내 주소
    # database 연결
    database = mongoClient["gatheringdatas"]
    # collection 작업
    collection = database['courtauction']
    return collection

# iframe으로 전환
browser.switch_to.frame('indexFrame')

# 메뉴 - 경매물건 : #menu > h1:nth-child(5)
selector_element = '#menu > h1:nth-child(5)'
element_auction_item = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
element_auction_item.click()
index = [0, 1, 2]  # 법원 3개
for i in index :
    # 지역 선택 : #idJiwonNm
    selector_element = '#idJiwonNm'
    element_choose_region = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
    Select(element_choose_region).select_by_index(i)
    # 검색 클릭 시 : #contents > form > div.tbl_btn > a:nth-child(1) > img
    search_element = 'div.tbl_btn > a:nth-child(1)'
    element_click_search = browser.find_element(by=By.CSS_SELECTOR, value=search_element)
    element_click_search.click()
    time.sleep(2)   # 화면 완성 term

# page_number = 1
# while True:
#     try:
#         # 페이지 번호가 있는 버튼을 찾아서 클릭
#         page_button = driver.find_element_by_xpath(f"//a[contains(text(), '{page_number}')]")
#         driver.execute_script("arguments[0].click();", page_button)
        
#         # 페이지 번호 증가
#         page_number += 1
#     except NoSuchElementException:
#         # 해당 페이지 번호의 버튼이 없으면 반복 종료
#         break


    #contents > div.table_contents > form:nth-child(2) > div > div.page2 > a > span : 페이지 번호 정보(2페이지부터)
    num_page = browser.find_elements(by=By.CSS_SELECTOR, value='form:nth-child(2) > div > div.page2 > a > span')
   
    for j in range(len(num_page)+1) :  # 페이지 수 오차 조정을 위한 보정치 +1 추가 / range : 범위(영역) 제한(설정) / len(길이,개수) : 해당 법원 페이지 수 확인을 위함 
    # range(len(num_page))
    # range(0, 9)
    # start:
    # 0
    # step:
    # 1
    # stop:
    # 9
    # range(len(num_page)+1)
    # range(0, 10)
    # start:
    # 0
    # step:
    # 1
    # stop:
    # 10

    ######## 사건번호, 소재지 및 내역 정보값 가져오기




    # 페이지 넘기기 : #contents > div.table_contents > form:nth-child(2) > div > div.page2 > span
        num_page = browser.find_elements(by=By.CSS_SELECTOR, value='form:nth-child(2) > div > div.page2 > a > span')
        if j < len(num_page) :
            num_page[j].click()
        else :
            break
        pass
    
    # 이전 버튼 클릭
    selector_element = 'div > a:nth-child(5) > img'
    element_click_previous = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
    element_click_previous.click()   # url 옆에 뒤로 가기 버튼이 아닌 홈페이지 내 검색 후 별도의 이전버튼을 클릭하기 위함이라 back을 사용하지 않음
    time.sleep(2)
    #contents > div.table_contents > form:nth-child(1) > div > div > a:nth-child(5) > img


pass

# 브라우저 종료
browser.quit()