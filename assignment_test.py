import re
from urllib.request import urlopen, URLError
from bs4 import BeautifulSoup


class Testy:
    def __init__(self):
        self.name = None
        self.test = 1

    def run(self):
        try:
            html = urlopen('http://www.nytimes.com')
        except URLError:
            print('URLERROR: URL is not responding. Please check the URL')
        else:
            bs = BeautifulSoup(html, 'lxml')
            self.name = bs.find_all(**{
                'name': 'a',
                'attrs': {'href': re.compile('nytimes')},
            })


test1 = Testy()
test1.run()
test1.test = 'a'
test2 = Testy()
test2.run()
print(test2.test)
