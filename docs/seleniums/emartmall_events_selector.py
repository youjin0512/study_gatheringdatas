# 클릭해서 하는 방법
# 태그를 정확하게 읽고서 하는 방법

# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=1
# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=2
# ...
# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=10

# * 웹 크롤링 동작      # 셀레니움에서 웹드라이버 임포트
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.chrome.options import Options

# Chrome 브라우저 옵션 생성
chrome_options = Options()

# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
# --user-agent : 내가 누구인지 나에 대한 정보를 서버에 넘김

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory), options=chrome_options)

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
# for page_number in [1,2,3,4,5,6] :       # page numbers
for page_number in range(1,7) :       # page numbers
    url = "https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214719&page={}".format(page_number)
    browser.get(url)
    time.sleep(3)   # 3 : 3초 / 다음페이지 로딩하는데 3초 정도 시간을 준다
    # - html 파일 받음(and 확인)
    html = browser.page_source
    pass


# - 가능 여부에 대한 OK 받음
pass
# print(html)

# - 정보 획득
pass
browser.save_screenshot('./formats_source.code_screenshotbyrun.png')

# 브라우저 종료
browser.quit()