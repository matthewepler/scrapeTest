from urllib.request import urlopen, URLError
from urllib.parse import urlencode

from scraper import Scraper


class Controller:
    """ Defines the page and parameters used for scraping """

    def __init__(self, url, params={}):
        """ Set the base_url and base_params when creating new instance """
        self.base_url = url
        self.params = params
        self.collections = []
        self.scrapers = []
        self.html = None

    def update_url(self, url):
        """ Change the url for scraping by passing in a string """
        if url is not None:
            self.base_url = url

    def set_params(self, params):
        """ Set the params used in the request by passing in key/value pairs 
        (dictionaries). This overwrites existing params. """
        if params is not None:
            self.params = params

    def update_param(self, key, value):
        """ Change the value of a single param """
        if key is not None and value is not None and key in self.params:
            self.params[key] = value

    def delete_param(self, key):
        """ Remove a key/value pair from the params dictionary """
        del self.params[key]

    def create_collection(self, name):
        """ Create a named container for alike results """
        self.collections.append({
            'name': name,
            'data': [],
        })

    def get_collection(self, name):
        for c in self.collections:
            if c['name'] == name:
                return c

    def add_to_collection(self, name, data):
        """ Add data to a collection of similar data """
        c = self.get_collection(name)
        if c is not None:
            c['data'].append(data)
        else:
            raise ValueError(
                """
                You are attempting to update a collection that 
                does not exist. Check the name of the collection you
                are trying to udpate.
                """
            )

    def scraper(self, elem=None, attr=None, s_filter=None):
        """ Create a scraper instance and add it to the scraper list """
        new_scraper = Scraper(elem, attr, s_filter)
        self.scrapers.append(new_scraper)
        return new_scraper       

    def connect(self):
        """ create a URL and attempt to fetch HTML data """ 
        try:
            if self.params is not None:
                self.html = urlopen(
                    self.base_url, data=urlencode(self.params).encode('ascii')
                )
            else:
                self.html = urlopen(self.base_url)
        except URLError:
            print('URLERROR: URL is not responding. Please check the URL')
        else:
            return self.html.code

    def run_all_scrapers(self):
        """ Run all Scraper instances in Controller's scrapers list """
        for s in self.scrapers:
            s.run(self.html)

    def run_scraper(self):
        """ Run a single Scraper """
        # -- TO-DO --
        pass

    def print_collections(self):
        """ Print all collections and their data 
        in the order they were added. """

        """ A collection is a list of lists """
        for collection in self.collections:
            print(collection['name'])
            print('{} item(s)'.format(len(collection['data'])))
            print('=' * len(collection['name']))
            for d in collection['data']:
                print(d)
                for item in d:
                    print('\t', item)
            print('\n')
