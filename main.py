"""
Web Scraping Tool

Scrapes web sites for nodes, cleans the results, and outputs to files.

Author: Matthew Epler, 2016
"""
import re
from controller import Controller


base_url = 'http://www.nytimes.com'
params = None
iterator_start = None
iterator_current = iterator_start
iterator_increm = None
iterator_end = None


def main():
    """Initializes and runs scraping tasks for a specific website. """

    # The Controller object creates and runs multipleScrapers. 
    # The data returned from the Scrapers is organized into collections.
    c = Controller(base_url, params)
    c.create_collection('menus')
    c.create_collection('links')
    c.create_collection('titles')

    # Define the type of data you want to scrape by creating Scraper objects
    all_navs = c.scraper('nav')
    links = all_navs.sub_scraper('a', 'href', re.compile('nytimes'))

    while c.connect() == 200: 
        c.run_all_scrapers()
        print(all_navs.raw_data)
        print('*' * 50)
        print(links.raw_data)
        c.add_to_collection(
            'menus',
            {
                'name': 'nav_menus',  # iterator_current + 
                'data': all_navs.raw_data,
            }
        )  
        # A single scraper can be used to contribute to multiple collections
        c.add_to_collection(
            'links',
            {
                'name': 'internal_links',  # iterator_current + 
                'data': links.clean('attr', 'href'),
            }
        ) 
        c.add_to_collection(
            'titles',
            {
                'name': 'nav_text',  # iterator_current + 
                'data': links.clean('text'),
            }
        )

        # update incrementer & params as necessary
        if iterator_start is not None and iterator_increm > 0:
            if iterator_current < iterator_end:
                # -- TO-DO -- 
                # update params with increment_current += iterator_increm
                # c.params = {}
                pass
        else:
            break

    if iterator_end is not None and iterator_current >= iterator_end:
        print('End of iterator range reached.')

    print('Scraping complete.')

    # For debugging or your viewing pleasure...
    # c.print_collections()

    # -- output to filetype, single collection --
    # -- output to filetype, multiple collections --
    # -- output to filetype, all collections --


if __name__ == '__main__':
    main()

# NOTE: You do not need a Controller or collection to run a Scraper. 
#
# from scraper import Scraper
# from urllib.request import urlopen, URLError
# from urllib.parse import urlencode
# s = Scraper('nav', 'id', 'mini-navigation')
# print('SCRAPER RUN WITHOUT CONTROLLER OR COLLECTION')
# if params is not None:
#     print(urlopen(
#         base_url, data=urlencode(params).encode('ascii')
#     ))
# else:
#     print(s.run(urlopen(base_url)))
