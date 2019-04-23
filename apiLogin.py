import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

#네이버 외부ID로 로그인 내역 가져오기

#로그인 유저정보
LOGIN_INFO = {
    'id': 'sixtynineee',
    'pw': 'dlekdms!1711',
    #'user-submit': rep.quote_plus('로그인'),
    #'user-cookie': 1
}

#Session 생성, WITH 구문안에서 유지
with requests.Session() as s:
    login_req = s.post('https://nid.naver.com/nidlogin.login', data=LOGIN_INFO)
    #html 소스 확인
    #print('login_req', login_req.text)
    #Header 확인
    #print('headers', login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('https://nid.naver.com/user2/help/externalAuth.nhn?lang=ko_KR')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())
        apiList = soup.select('div')
        print(apiList)
        # for i in apiList:
        #     if i.string is not None:
        #         #DB INSERT, 엑셀로저장, 텍스트가공
        #         print(i.string)
