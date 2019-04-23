import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

r = requests.get('https://api.github.com/events')
#requests시 요청에 에러가 발생했을때 예외처리해준다
#r.raise_for_status()
#print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'kim', domain='httpbin.org', path='/cookies')


#r = requests.get('http://httpbin.org/cookies',cookies=jar)
#r.raise_for_status()
#print(r.text)

#r = requests.get('https://github.com', timeout=3)
#print(r.text)

#r = requests.post('http://httpbin.org/post', data= {'name':'kim'}, cookies=jar)
#print(r.text)

payload1 = {'key1':'val1', 'key2' :'value2'} #dict , dictionary형식을 가장 많이 쓴다.
payload2 = (('key1','value1'),('key2','value2')) #tuple
payload3 = {'some':'nice'}

r = requests.post('http://httpbin.org/post', data = payload1) #form데이터형태로 들어옴
print(r.text)

#json을 활용한 post방식으로 보낼때에는 json dump 파일을 활용해야한당.
r = requests.post('http://httpbin.org/post', data =json.dumps(payload3))
print(r.text)
