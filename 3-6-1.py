# selenium 사용 이유 : 자동화된 웹 어플리케이션을 사용하기 위핸 프레임워크
# requests(fake-useragent) : 웹브라우저 없이 사용해서 해당 모듈 이용

#환경설정
# 1. selenium + 크롬
# 2. selenium + 파이어폭스
# 3. selenium + PhantomJS(현재는 지원안하지만 이형식으로 만들어져 있는 것들이 많음)
# web driver를 다 다운로드 받아야 한다.

import sys
import io
from selenium import webdriver
# webdriver로 어떤 브라우저를 사용해서 할 건지 선택하게 된다
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

driver = webdriver.PhantomJS(executable_path = "C:/Python/workspace/section3/webdriver/phantomjs/phantomjs")
# 암묵적으로 5초간 쉬어가기 위한 함수. 리소스가 빠르게 로딩이 되면 실행하지 않고 그냥 넘어간다.
driver.implicitly_wait(5)

driver.get('https://google.com')
#해당 사이트 스크린샷을 아래 경로에 남긴다.
driver.save_screenshot('c:/website1.png')

driver.implicitly_wait(5)

driver.get('https://www.naver.com')
driver.save_screenshot("c://website2.png")

driver.quit()
print('스크린샷 완료')
#drivers가 내부적으로 브라우저를 핸들링하는 것을 확인할 수 있다.
