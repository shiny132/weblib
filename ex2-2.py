# GET 방식으로 웹 서버에 요청 보내기
from urllib.request import urlopen

f = urlopen('http://www.example.com?a=10&b=20')
print(f.read())