import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# webdriver로 어떤 브라우저를 사용해서 할 건지 선택하게 된다
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

driver = webdriver.Chrome(executable_path = "C:/Python/workspace/section3/webdriver/chrome/chromedriver")
driver.set_window_size(1920,1280)
driver.implicitly_wait(3)

driver.get('http://www.encar.com/index.do')
time.sleep(3)
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="manufact"]/a').click()
time.sleep(3)
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="manufactListText"]/ul[1]/li[3]/a').click()
time.sleep(3)
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="seriesItemList"]/li[4]/a').click()
time.sleep(3)
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="mdlItemList"]/li[2]/a').click()
time.sleep(3)
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="indexSch1"]/div[1]/a').click()
time.sleep(3)
driver.implicitly_wait(5)
# driver.find_element_by_name('pwd').send_keys('pw')
# driver.implicitly_wait(1)
# driver.find_element_by_xpath('//*[@id="wp-submit"]').click()
