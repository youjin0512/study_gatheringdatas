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
url = "https://play.google.com/store/search?q=%ED%97%AC%EC%8A%A4%EC%BC%80%EC%96%B4%EC%95%B1&c=apps&hl=ko-KR"
browser.get(url)

# - 정보 획득
from selenium.webdriver.common.by import By
# 앱 제조회사 리스트 : div > a.Si6A0c.Gy4nib
element_companies = browser.find_elements(by=By.CSS_SELECTOR, value="div > a.Si6A0c.Gy4nib")

for company in element_companies :
    company.click()
    time.sleep(1)
    pass
pass    

# 브라우저 종료
browser.quit()