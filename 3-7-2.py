import sys
import io
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class NcafeWriteAtt:
    #초기화실행(webdriver 설정)
    def __init__(self): # intializing해서 한번만 초기화 할 것이므로 self선언
        # chrome_options = Options()
        # chrome_options.add_argument("--headless") #CLI (User-agent)
        self.driver = webdriver.Chrome(executable_path="c:/Python/workspace/section3/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

    #네이버카페 로그인 && 출석체크
    def writeAttendCheck(self):
        self.driver.get('https://logins.daum.net/accounts/loginform.do?url=http%3A%2F%2Fcafe.daum.net%2F_c21_%2Fmemo_list%3Fgrpid%3D1QVVa%26fldid%3D7Gqk&category=cafe&t__nil_navi=login')
        self.driver.find_element_by_name('id').send_keys('cute-merry')
        self.driver.find_element_by_name('pw').send_keys('duwkekdms')
        self.driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        #self.driver.implicitly_wait(30) #서버에서 response될때까지 30초간 기다리겠다. --> 얘때문에 안됨...
        self.driver.get('http://cafe.daum.net/to.basic/7Gqk') #버스커버스커 카페
        self.driver.implicitly_wait(30)
        # 네이버 카페는 iframe으로 이루어져 있어서 글작성을 원하는 블럭에 접근이 어렵다. 따라서 frame으로 전환이 필요하다.
        self.driver.switch_to_frame('down')
        self.driver.find_element_by_id('memo_write').send_keys('반갑습니다.')
        self.driver.find_element_by_xpath('//*[@id="memoForm"]/div/table/tbody/tr[1]/td[2]/a[1]/span[2]').click()
        time.sleep(3)

        #소멸자
    def __del__(self):
        #self.driver.close() #현재 실행 포커스된 영역을 종료
        self.driver.quit()  #Selenium의 전체 프로그램 종료
        print("Removed driver Object")
#실행

if __name__=='__main__':
    #객체생성
    a = NcafeWriteAtt()
    #시작시간
    start_time = time.time()
    #프로그램 실행
    a.writeAttendCheck()
    #종료시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체 소멸
    del a
