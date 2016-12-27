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


if __name__ == '__main__':
    main()
