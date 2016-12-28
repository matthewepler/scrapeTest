"""
Searches for and returns nodes

Takes a type, attribute (opt), and filter (opt)
Returns a list of nodes
"""


class Scraper:
    """Searches page for given elements using filters and returns whoe nodes"""

    def __init__(self, elem_type, attribute, search_filter):
        self.type = elem_type
        self.attr = attribute
        self.filter = search_filter

    def set_element_type(self, elem_type):
        self.type = elem_type

    def set_attribute(self, attribute):
        self.attr = attribute

    def set_search_filter(self, search_filter):
        self.filter = search_filter

    def add_scraper(self):
        pass
