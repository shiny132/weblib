from urllib.request import urlopen
from html.parser import HTMLParser
from http.client import HTTPConnection

file_path = '__result__/crawling/'
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
    data = response.read().decode(charset)
    response.close()
    print('\n>>>>>>> Fetch Image from', url)
    parser = ImageParser()
    parser.feed(data)
    dataset = set(x for x in parser.result)
    datas = '\n'.join(sorted(dataset))
    datas = datas.split("\n")

    for data in datas:
        conn = HTTPConnection('www.google.co.kr')
        file_name = file_path + data.split('/')[-1]
        conn.request('GET', data)
        result = conn.getresponse()
        print(result.status, result.reason)

        with open(file_name, 'wb', ) as outfile:
            outfile.write(result.read())

if __name__ == '__main__':
    main()
