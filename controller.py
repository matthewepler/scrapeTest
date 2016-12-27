class Controller:
    """Defines the page and parameters used for scraping"""
    def __init__(self, url, params={}):
        self.base_url = url
        self.base_params = params

    def update_url(self, url):
        """Change the url for scraping by passing in a string"""
        if url is not None:
            self.base_url = url

    def update_params(self, params):
        """Change the params used in the request by passing in key/value 
        pairs (dictionaries)"""
        if params is not None:
            self.base_params = params
