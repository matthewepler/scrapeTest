import re
from urllib.request import urlopen, URLError
from urllib.parse import urlencode
from bs4 import BeautifulSoup

base_url = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php'
params = {
    't': 12591,  # topicId
    'postdays': '0',
    'postorder': 'asc',
    'start': str(300)   # posts startIndex, e.g. for 51-100, 51 is the startIndex
}

try:
    # html = urlopen(base_url, data=urlencode(params).encode('ascii'))
    html = urlopen('http://www.nytimes.com')
except URLError:
    print('URLERROR: URL is not responding. Please check the URL')
else:
    print(html.code)
    bs = BeautifulSoup(html, 'lxml')
    results = bs.find_all(**{
        'name': 'a',
        'attrs': {'href': re.compile('nytimes')},
    })
    # details = results.find(**{
    #     'name': 'nav',
    #     'attrs': {'id': 'mini-navigation'},
    # })
    print(results)
    


"""

base_url = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php'
params = {
    't': 12591,  # topicId
    'postdays': '0',
    'postorder': 'asc',
    'start': str(0)   # posts startIndex, e.g. for 51-100, 51 is the startIndex
}
iterator_start = params['t']
iterator_current = iterator_start
iterator_end = None
iterator_increm = 15

"""    