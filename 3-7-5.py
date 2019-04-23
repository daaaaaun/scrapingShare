import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#google계정을 통한 로그인
class NcafeMemberEx:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless") #CLI (User-agent)
        self.driver = webdriver.Firefox(firefox_options=firefox_options, executable_path="C:/Python/workspace/section3/webdriver/firefox/geckodriver")
        #self.driver.implicitly_wait(5)

    #다음카페 회원내역 추출
    def getMemberList(self):
        self.driver.get('https://accounts.google.com/signin/v2/identifier?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        self.driver.find_element_by_name('identifier').send_keys('geeeeekirl@gmail.com')
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]/content').click()
        time.sleep(3)
        self.driver.find_element_by_name('password').send_keys('ekdms556')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]/content').click()
        time.sleep(3)
        self.driver.get('https://myaccount.google.com/permissions?utm_source=google-account&utm_medium=web')
        soup = BeautifulSoup(self.driver.page_source,'html.parser')
        return soup.select('#sign-in > div.hyMrOd > div > div > div.URz83d.WRlqaf > div > div.CMEZce')

    #출력
    def printMemberList(self,list):
        print("[google계정을 통한 로그인]")
        for i in list:
            print(i.string.strip())

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
    a.printMemberList(a.getMemberList())
    #종료 시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체 소멸
    del a
