# POST 방식으로 웹 서버에 요청 보내기
from urllib.request import urlopen
from html.parser import HTMLParser
import urllib

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print(tag)
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                # print(value)
                self.result.append(value)


def main():
    url = 'http://www.google.co.kr'

    response = urlopen(url)
    charset = response.headers.get_content_charset()
    # print(charset)
    data = response.read().decode(charset)
    response.close()

    print('\n>>>>>>> Fetch Image from', url)

    parser = ImageParser()
    parser.feed(data)  # 파서에 데이터를 주는것
    dataset = set(x for x in parser.result)  # 집합 만들기(set로 만들기)
    print('\n'.join(sorted(dataset)))  # 정렬하면서 String 값으로 변환
    # urllib.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")


if __name__ == '__main__':
    main()