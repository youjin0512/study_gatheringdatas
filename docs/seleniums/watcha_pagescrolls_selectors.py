# * 웹 크롤링 동작      # 셀레니움에서 웹드라이버 임포트
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://pedia.watcha.com/ko-KR/contents/m5ZlbBL/comments")

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 한 페이지씩 이동
element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")   # element_body이 scroll되서 정보가 들어감

previous_scrollHeight = 0
while True : 
    element_body.send_keys(Keys.END)

    current_scrollHeight = browser.execute_script("return document.body.scrollHeight")    # execute_script : chrome console에서 동작시키기 위함
    if previous_scrollHeight >= current_scrollHeight :     # previous가 current보다 크거나 같을 때 break
        break
    else :
         previous_scrollHeight = current_scrollHeight      # currnet를 previous라는 변수에 값 할당
    time.sleep(1)
    pass
# browser.save_screenshot('./formats_source.code_screenshotbyrun.png')

# 브라우저 종료
browser.quit()