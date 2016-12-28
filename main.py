"""
Web Scraping Tool

Scrapes web sites for nodes, cleans the results, and outputs to CSV.

Author: Matthew Epler, 2016
"""

from controller import Controller


baseURL = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php'
params = {
    't': str(12591),  # topicId
    'postdays': '0',
    'postorder': 'asc',
    'start': str(0)   # startIndex
}


def main():
    """Initializes and runs scraping tasks for a specific website"""
    c = Controller(baseURL, params)
    c.create_collection('posts')
    
    # define what kinds of elements you want to target
    # ?? should Scraper be a class within Controller?


if __name__ == '__main__':
    main()


# create a controller - holds url and params
# create scrapers for every kind of target I want on that page
# define cleaner method(s) for each scraper -> designate type and destination
# define printer class to show what is in each collection
# write collections to CSV

