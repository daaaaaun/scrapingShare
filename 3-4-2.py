import sys
import io
from bs4 import BeautifulSoup
import requests
import urllib.parse as rep
import os
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

#로그인 유저정보
LOGIN_INFO = {
    'user_id': 'outsider7224',
    'user_pw': 'dmsrleoqkr7974!',
    'user-submit': rep.quote_plus('로그인'),
    'user-cookie': 1
}

#Session 생성, WITH 구문안에서 유지
with requests.Session() as s:
    login_req = s.post('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2F%2Fwww.inflearn.com%2F', data=LOGIN_INFO)
    #html 소스 확인
    #print('login_req', login_req.text)
    #Header 확인
    #print('headers', login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('http://www.inflearn.com/members/outsier7224/')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())
        badges = soup.select("div.badges > ul > li > a > img")
        for i,z in enumerate(badges,1):
            #print(z)
            fullFileName = os.path.join("c:/",str(i)+'.jpg')
            req.urlretrieve(z['src'], fullFileName)
