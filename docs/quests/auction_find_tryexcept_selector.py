# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
browser.get("https://corners.auction.co.kr/corner/categorybest.aspx")  # 해석 : 브라우저 안에서 이 url, element를 가져온다

# - 가능 여부에 대한 OK 받음
pass

# - 정보 획득
from selenium.webdriver.common.by import By
selector_value = "div.info"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)   # value : 전체

for element_item in element_bundle[10:41] :     # element_bundle : list[webelement]
    #상품 제목(title)
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value="em")    # value = 타이틀 / 변수로 담아서 str으로 넣으면 좋음
    title = element_title.text
    # 상품 판매 원가(old price) (try~except 포함)
    try :   
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value="span")    # value : element 접근자
        old_price = element_old_price.text    # old_price : 이 부분에 값이 있거나 공란으로 들어가야함 (공란인 이유? : old price가 없는 경우 있어서)
        pass    # 정식 코드
    except :
        old_price = ""     # 특정 항목에서는 태그가 없을 수 있다
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass    # try나 except이 끝난 후 무조건 실행 코드
    # 변경가격(sale price)
    element_sale_price = element_item.find_element(by=By.CSS_SELECTOR, value="span.sale")    # value = sale price / 변수로 담아서 str으로 넣으면 좋음
    sale_price = element_sale_price.text
    # 배송방법(delivery)
    smiledelivery = ""  # 초기화
    freedelivery = ""  # 초기화
    try:   
        element_smiledelivery = element_item.find_element(by=By.CSS_SELECTOR, value="div.icons.ic_smiledelivery")    # value : 스마일배송
        smiledelivery = element_smiledelivery.text
    except: None
    try:
            element_freedelivery = element_item.find_element(by=By.CSS_SELECTOR, value="div.icons.ic_free")    # value : 무료배송
            freedelivery = element_freedelivery.text
    except: None
    pass  # 무료 배송도 스마일 배송도 아닌 경우
print("title : {}, old price : {}, sale price : {}".format(title, old_price, sale_price))
print("smiledelivery : {}, freedelivery : {}".format(smiledelivery, freedelivery))

pass

# 브라우저 종료
browser.quit()