import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# webdriver로 어떤 브라우저를 사용해서 할 건지 선택하게 된다
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

firefox_options = Options()
firefox_options.add_argument("--headless") #CLI 환경으로 설정

#chrome으로 CLI환경을 돌리기 위해서 driver에도 chrome_options설정을 해줘야 한고 execute_path를 통해서 즉시 실행 하기 휘한 path 매핑이 필요
#driver = webdriver.Firefox(firefox_options=firefox_options, executable_path =r"C:/Python/workspace/section3/webdriver/firefox/geckodriver")
driver = webdriver.Chrome(executable_path = "C:/Python/workspace/section3/webdriver/chrome/chromedriver")
driver.set_window_size(1920,1280)
driver.implicitly_wait(3)

driver.get('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F')
#화면을 제대로 로딩시키기위해 멈주는 시간 5초 제공
time.sleep(7)
driver.implicitly_wait(3) #실질적인 로딩이 되도록 암묵적 기다림시간 3초 제공

driver.find_element_by_name('log').send_keys('id')
driver.implicitly_wait(1)
driver.find_element_by_name('pwd').send_keys('pw')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="wp-submit"]').click()
