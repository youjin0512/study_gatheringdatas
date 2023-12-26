# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))  

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033")  

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source            # browser = class, class에는 변수와 function --> page_source : function
print(html)

# - 정보 획득             # 정보 획득 시 거의 고정되는 문구
from selenium.webdriver.common.by import By

# ## 하나(단수)의 element 가져오기
# selector_value = "#ty_thmb_view > ul > li:nth-child(21) > div > a > div.mnemitem_tit > span.mnemitem_goods_tit"   # parameter 변수로 담기
# element_path = browser.find_element(by=By.CSS_SELECTOR, value=selector_value)   # element의 괄호 안은 어떤 parameters다  / By.CSS_SELECTOR - import 해줘야만 동작
# # browser.find_element(By.CSS_SELECTOR, "#ty_thmb_view > ul > li:nth-child(21) > div > a > div.mnemitem_tit > span.mnemitem_goods_tit")      # <-- key와 value 값 명확히 알고 있을 때 사용
# type(element_path)    #디버깅 모드에서 왼쪽 문구 입력
# <class 'selenium.webdriver.remote.webelement.WebElement'>

# get text in tag (tag 안에 text 가져오기)
# element_path.text
# # element_path.text     #디버깅 모드에서 왼쪽 문구 입력
# # '건강한간식 순살듬뿍 고구마 오리말이 300g'
# element_path.get_attribute('class')   #디버깅 모드에서 왼쪽 문구 입력
# 'mnemitem_goods_tit'
pass

## 여러개(복수) elements 정보 가져오기  <-- 어떤 find를 했을 때 정보가 여러 개 라는 의미
selector_value = "span.mnemitem_goods_tit"
elements_path = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)  # find_element's' 추가 / elements_path에도 's' 추가
type(elements_path)
# <class 'list'>
# type(elements_path[0])
# <class 'selenium.webdriver.remote.webelement.WebElement'>
# elements_path[0].text
# # '시리우스 펫퓸 반려견 러블리플라워 샴푸 500ML'
# elements_path[1].text
# '시리우스 펫퓸 반려견 드라이풋샴푸 270ML'
for webelement in elements_path :
    title = webelement.text
    print("{}".format(title))
    pass
pass

# 브라우저 종료
browser.quit()