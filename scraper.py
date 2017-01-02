"""
Searches for and returns nodes

Takes a type, attribute, and filter
Returns a list of nodes
"""
from datetime import datetime
from bs4 import BeautifulSoup

from cleaners import cleaners


class Scraper:
    """ Searches page for given elements using filters 
    and returns whole nodes """

    def __init__(self, elem_type=None, attribute=None, search_filter=None):
        """ Create Scraper instance with optional element type, attribute, 
        and search_filter. Filter can be a string or regex expression """
        self.type = elem_type
        self.attr = attribute
        self.filter = search_filter
        self.sub_scrapers = []
        self.raw_data = None
        self.clean_data = None
        self.cleaners = cleaners
        self.temp = 'tempy'

    def set_element_type(self, elem_type):
        """ manually set or change the type of node element to scrape """
        self.type = elem_type

    def set_attribute(self, attribute):
        """ manually set or change the node element attribute to scrape """
        self.attr = attribute

    def set_search_filter(self, search_filter):
        """ manually set or change the filter used to find node elements """
        self.filter = search_filter

    def sub_scraper(self, elem_type=None, attribute=None, search_filter=None):
        """
        Add a Scraper object that is associated with this one.
        Used for Organizational purposes.  
        """
        new_sub = Scraper(elem_type, attribute, search_filter)
        self.sub_scrapers.append(new_sub)
        return new_sub

    def run(self, html):
        """ Use scraping library and object vars to collect nodes """
        bs = BeautifulSoup(html, 'lxml')
        self.raw_data = bs.find_all(**{
            'name': self.type,
            'attrs': {
                'class_' if self.attr == 'class' else self.attr:
                self.filter
            },
        })
        # -- ??? -- returns same for both Scraper instances. 
        # It's overwriting the second time through.
        # Shouldn't be a namespace issue because I'm using instance vars
        #   in __init__()
        self.temp = datetime.now().microsecond  # see clean() for the print()

        if len(self.sub_scrapers) > 0:
            for s in self.sub_scrapers:
                s.run(html)

        return self.raw_data

    def clean(self, cleaner_name, item=None):
        """ Return data from nodes in desired format """
        print(self.temp)
        if cleaner_name in self.cleaners:
            self.clean_data = self.cleaners[cleaner_name](self.raw_data, item)
            return self.clean_data
        else:
            raise AttributeError('Specified cleaner does not exist')

    def add_cleaner(self, name, func):
        """ Add a custom func to the cleaners dictionary """
        self.cleaners[name] = func
