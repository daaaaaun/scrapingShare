import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# webdriver로 어떤 브라우저를 사용해서 할 건지 선택하게 된다
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless") #CLI 환경으로 설정

#chrome으로 CLI환경을 돌리기 위해서 driver에도 chrome_options설정을 해줘야 한고 execute_path를 통해서 즉시 실행 하기 휘한 path 매핑이 필요
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path =r"C:/Python/workspace/section3/webdriver/chrome/chromedriver")
#driver = webdriver.Chrome(executable_path = "C:/Python/workspace/section3/webdriver/chrome/chromedriver")
#브라우저 사이즈를 임의로 지정할 수 있다
#driver.set_window_size(1920,1280)
# 암묵적으로 5초간 쉬어가기 위한 함수. 리소스가 빠르게 로딩이 되면 실행하지 않고 그냥 넘어간다.
#driver.implicitly_wait(5)

driver.get('https://google.com')
#해당웹사이트에 방문 후 5초간 정지한다. 모듈 import 필요함
#time.sleep(5)  #chrome을 CLI환경으로 셋팅해 브라우저 없을경우 time이 필요없다. 멈출필요 ㄴㄴ
#해당 사이트 스크린샷을 아래 경로에 남긴다.
driver.save_screenshot('c:/website_ch.png')
#driver.implicitly_wait(5)

driver.get('https://www.naver.com')
#time.sleep(5)
driver.save_screenshot("c:/website_ch2.png")

driver.quit()
print('스크린샷 완료라구욧')
#drivers가 내부적으로 브라우저를 핸들링하는 것을 확인할 수 있다.

#phantomjs는 화면에 표시되는 것 없이 cli(command line interface) 환경으로 움직인다. 속도가 빠름
#chrome과 firefox도 CLI환경을 제공한다
