# * 웹 크롤링 동작
from selenium import webdriver   # 셀레니움에서 웹드라이버 임포트

# 1. chrome browser 열기
browser = webdriver.Chrome()       # chrome 초기 생성자(class의 생성자) / 클래스의 모든 자원이 return됨 / 브라우저를 열어서 화면을 띄운것과 같음 / browser라는 변수가 browser가 됨

# 2. 주소 https://www.w3schools.com/ 입력
browser.get("https://www.w3schools.com/")    # 브라우저에 링크 넣고 엔터까지 친게 get의 기능

# 3. 가능 여부에 대한 OK 받음         # 위 주소 잘 열리는지 확인하는것이 OK 사인 받은거
pass
# 4. html 파일 받음(and 확인)
html = browser.page_source
print(html)

# 5. 정보 회득
pass
# 6. 브라우저 종료
browser.quit()