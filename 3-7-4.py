#로그인 후 회원정보 내역을 가져온다.
import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup
import requests
#fiddler를 통해서 소스에서 들어오고 나가는 HTTP통신에 관련된 자료를 확인할 수 있다.

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeMemberEx:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        # firefox_options = Options()
        # firefox_options.add_argument("--headless") #CLI (User-agent)
        self.driver = webdriver.Firefox(executable_path="C:/Python/workspace/section3/webdriver/firefox/geckodriver")
        #self.driver.implicitly_wait(5)

    #다음카페 회원내역 추출
    def getMemberList(self):
        self.driver.get('https://logins.daum.net/accounts/loginform.do?url=http%3A%2F%2Ftop.cafe.daum.net%2F')
        self.driver.find_element_by_name('id').send_keys('cute-merry')
        time.sleep(3)
        self.driver.find_element_by_name('pw').send_keys('duwkekdms')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        time.sleep(3)
        self.driver.get('http://cafe.daum.net/_c21_/memberlist?grpid=1QVVa')
        #self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafeon')
        soup = BeautifulSoup(self.driver.page_source,'html.parser')
        print(soup.prettify())
        #html parsing을 해야하기 떄문에 beautifulsoup이 필요함

    # 소멸자
    def __del__(self):
        #self.driver.close() #현재 실행 포커스 된 영역을 종료
        self.driver.quit()  #Seleninum 전체 프로그램 종료
        print("Removed driver Object")

#실행
if __name__ == '__main__':
    #객체 생성
    a = NcafeMemberEx()
    #시작 시간
    start_time = time.time()
    #프로그램 실행
    a.getMemberList()
    #종료 시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체 소멸
    del a
