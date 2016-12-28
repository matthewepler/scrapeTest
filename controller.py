class Controller:
    """ Defines the page and parameters used for scraping """

    def __init__(self, url, params={}):
        """ Set the base_url and base_params when creating new instance """
        self.base_url = url
        self.params = params
        self.collections = []
        self.scrapers = []

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

    def print_collections(self):
        """ Print all collections and their data 
        in the order they were added. """
        for collection in self.collections:
            print(collection.name)
            print('{} entries').format(len(collection.data))
            print('=' * len(collection.name))
            for d in collection.data:
                print(d)
            print('\n')
