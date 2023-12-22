#  * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()

browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://www.coupang.com/np/categories/185797")  

# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source            # browser = class, class에는 변수와 function --> page_source : function
print(html)

# - 정보 획득                        # 정보 획득 시 거의 고정되는 문구
from selenium.webdriver.common.by import By

## 여러개(복수) elements 정보 가져오기  <-- 어떤 find를 했을 때 정보가 여러 개 라는 의미
selector_value = "div.name"
elements_path = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)  # find_element's' 추가 / elements_path에도 's' 추가
type(elements_path)

for webelement in elements_path :
    title = webelement.text
    print("{}".format(title))
    pass
pass

# 브라우저 종료
browser.quit()

# 락앤락 리틀럽 마망 가열텀블러 아이보리 300ml, EJC723IVY
# 디즈니 앨리스 도자기 스태커블 티팟 세트, 혼합색상, 1세트
# 그로미미 원터치 스테인리스 빨대컵 300ml, 돗꼼 버터, 1개
# 포트메리온 보타닉가든 테라스 벨머그 4p, 혼합색상, 1세트
# 스탠리 어드벤쳐 진공 파인트 텀블러, 라벤더, 473ml
# 그로미미 원터치 스테인리스 빨대컵 300ml, 올리브 피스타치오, 1개
# 포트메리온 스포드 모리스엔코 해초 머그 세트 2p, 1세트
# 모슈 라떼 스트로우 텀블러, 화이트, 480ml, 1개
# 락앤락 메트로 밀폐 머그 텀블러, 코튼 캔디 핑크, 475ml, 1개
# 푸고 유아용 프리미엄 빨대컵 280ml, 블루, 1개
# 주니 유아용 자기주도 빨대컵 210ml, 화이트, 1개
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 풀, 887ml, 1개
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 포그, 1.18L, 1개
# 그로미미 원터치 스테인리스 체리쉬 빨대컵 200ml, 스윗피치, 1개
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 핑크더스트, 887ml, 1개
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 핑크더스트, 591ml, 1개
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 포그, 887ml, 1개
# 포트메리온 스포드 모리스엔코 블랙손 + 골든릴리 머그 세트 2p, 블랙손&골든릴리, 1세트
# 락앤락 스쿨핏 츄잉 원터치 텀블러, 핑크, 360ml
# 에디슨 온도 표시 원터치 분유 보온병, 브라운, 500ml, 1개
# 스탠리 어드벤쳐 퀜처 텀블러, 샴브레이, 591ml, 1개
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 블랙, 887ml, 1개
# 보르미올리 PLANER FLUTE 샴페인잔, 240ml, 4개
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 포그, 414ml, 1개
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 유칼립투스, 591ml, 1개
# 스탠리 클래식 진공 캠프 머그, 크림글로스, 354ml
# 스탠리 에어로라이트 진공 텀블러, 차콜, 473ml
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 오키드, 887ml, 1개
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 포그, 591ml, 1개
# 조지루시 원터치 미니 텀블러, 세이지 그린(GM), 200ml
# 스탠리 고 진공 보틀, 블랙, 709ml
# 락앤락 메트로 밀폐 머그 텀블러, 피코크 그린, 475ml, 1개
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 로즈쿼츠, 414ml, 1개
# 스탠리 에어로라이트 진공 텀블러, 블랙, 473ml
# 스탠리 고 진공 보틀, 해머톤 그린, 709ml
# 빌레로이앤보흐 보스톤 고블렛 중 310ml, 투명, 4개
# 락앤락 데일리 원터치 클립 텀블러, 라벤더, 550ml, 1개
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 크림, 414ml, 1개
# 락앤락 리틀럽 실리콘 빨대컵 200ml 세트 일반형 + 스파우트형, 스카이블루, 옐로우, 1세트
# 히카리 슬림 미니 보온보냉 스텐 텀블러, 그린, 300ml
# 칼딘 클린 티 핸디 보온보냉 텀블러 CT-01, 아이보리, 400ml
# 조지루시 심리스 보온보냉 원터치 텀블러, 카키(GD), 600ml
# JIN 홈카페 홈바 프리미엄 샴페인 글라스, 230ml, 6개
# 락앤락 메트로 티머그 400ml LHC4305, 라벤더(LHC4305LVOL), 1개
# 스탠리 고 진공 보틀, 화이트, 473ml
# 스탠리 고 진공 텀블러, 베리, 473ml
# 스탠리 GO 진공 보틀 473ml, 블랙
# 홈바 용품 8종 + 나무 거치대 세트, 혼합색상, 1세트
# 조지루시 보온보냉 원터치 텀블러, 매트 화이트, 600ml
# 락앤락 유아용 리틀럽 실리콘 빨대컵 200ml + 전용 빨대 2종 세트, 라벤더(컵/십자빨대), 옐로우(꺾인빨대), 1세트
# 락앤락 데일리 원터치 클립 텀블러, 블랙, 550ml
# 포트메리온 보타닉가든 신형 T형 커피잔 6인조, 랜덤 발송, 1세트
# 스탠리 퀜처 H2.0 플로우스테이트 텀블러, 샴브레이, 887ml, 1개
# 벨라쿠진 블랙라인 전동 와인오프너 풀 세트, 혼합색상, 1세트
# 아트웨어 퓨어 파퓰러 하이볼컵 600ml, 2개
# 스탠리 어드벤처 진공 머그, 민트, 236ml
# 스탠리 에어로라이트 진공 텀블러, 해머톤 그린, 473ml
# 조지루시 심리스 보온보냉 원터치 텀블러, 아이스 그레이(HL), 600ml
# 가스파드와리사 머그컵 4종 세트, 혼합색상, 1세트
# 에디슨 온도 표시 원터치 분유 보온병, 베이지, 500ml, 1개