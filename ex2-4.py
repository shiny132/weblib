# http.client.HttpConnection을 사용한 GET 방식 요청

from http.client import HTTPConnection

conn = HTTPConnection('www.example.com') # 도메인만 적어줌 ( http 제외 )
conn.request('GET', '/')

result = conn.getresponse() #상태값을 받음 (헤더에 있는 200 ok를 받음)
print(result.status, result.reason) #에러났을 떄 404는 status고 not found는 reason

data = result.read()
print(data)
