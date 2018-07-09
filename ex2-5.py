# http.client.HttpConnection을 사용한 GET 방식 요청

from http.client import HTTPConnection

conn = HTTPConnection('www.example.com') # 도메인만 적어줌 ( http 제외 )
conn.request('HEAD', '/')

result = conn.getresponse()
print(result.status, result.reason)

data = result.read()
print(len(data)) # 헤더만 보내므로 result는 비어있을 것
