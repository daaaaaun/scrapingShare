import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
#보안토큰으로 감싸져 있는 사이트에 로그인처리를 해서 정보를 가져온다.
#csrf Token: 파라미터를 가지고 자동으로 어떤 처리를 반족하는것을 방지하는 것. 랜덤으로 발행됨.
#위시캣 사이트 로그인 처리 후 정보 가져오는 

#요청 URL
URL = 'https://www.wishket.com/accounts/login/'
#Fake UserAgent 생성
ua = UserAgent()
# print(ua.ie)
# print(ua.chrome)
# print(ua.random)

with requests.session() as s:
#URL 연결 (요청을 하기전에 연결을 시도해서 csrfToken을 )
    s.get(URL)
#Login정보  Payload (request에 보낼 수 있다.)
    LOGIN_INFO= {
        'identification': 'cutemerry',
        'password': 'dlekdms!556',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }

#요청
    response = s.post(URL, data = LOGIN_INFO, headers={'User-Agent':str(ua.chrome), 'Referer': 'https://www.wishket.com/accounts/login/'})
    #HTML 결과확인
    #print('response', response.text)
    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        projectList = soup.select("div.contract > div.contract-data > div")

        for i in projectList:
             print(i.text)

#개발자의 tool, 서버에서 거절시 반환되는 값들을 잘 확인한 다음에 로그인처리를 해야한다.
