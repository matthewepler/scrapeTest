#!/usr/bin/env python3
import re
import unittest
from urllib.request import urlopen

from controller import Controller
from scraper import Scraper


class MainTests(unittest.TestCase):
    def test_one_plus_one(self):
        assert 1 + 1 == 2


class ControllerTests(unittest.TestCase):
    def setUp(self):
        """ Create an instance of Controller """
        self.c = Controller(
            url='http://www.google.com/#',
        )

    def test_update_url(self):
        """ Does the base_url string get overwritten when updated? """
        self.c.update_url('http://yahoo.com')
        self.assertIn('yahoo', self.c.base_url)

    def test_set_params(self):
        """ Does the params dictionary get overwritten when set? """
        self.c.set_params({
            'name': 'Matthew',
            'job': 'developer'
        })
        self.assertEqual('developer', self.c.params['job'])

    def test_update_param(self):
        """ Does changing a single param overwrite only that item? """
        self.c.set_params({
            'name': 'Matthew',
            'job': 'developer'
        })
        dict_len = len(self.c.params)
        self.c.update_param('job', 'model')
        self.assertEqual('model', self.c.params['job'])
        self.assertEqual(dict_len, len(self.c.params))

    def test_delete_param(self):
        """ Does deleting a param remove it entirely from the dict? """
        self.c.set_params({
            'name': 'Matthew',
            'job': 'developer'
        })
        dict_len = len(self.c.params)
        self.c.delete_param('job')
        self.assertNotIn('job', self.c.params)
        self.assertEqual(dict_len - 1, len(self.c.params))

    def test_create_collection(self):
        """ Can we createa new named dictionary and store it? """
        self.c.create_collection('titles')
        self.assertEqual('titles', self.c.collections[-1]['name'])
        self.assertEqual(len(self.c.collections[-1]['data']), 0)

    def test_add_scraper(self):
        """ Can we create an instance of the Scraper class? """
        self.c.scraper('a', 'class', 'nav')
        self.assertTrue(len(self.c.scrapers) == 1)
        self.assertIn('class', self.c.scrapers[0].attr)
        self.c.scraper('a', 'href', re.compile('nytimes'))
        self.assertTrue(len(self.c.scrapers) == 2)
        self.assertNotEqual(self.c.scrapers[0], self.c.scrapers[1])

    def test_add_to_collection(self):
        """ 
        Does adding to a collection create a nested dictionary in the
        correct collection? 
        """
        self.c.create_collection('links')
        self.c.add_to_collection(
            'links', 
            {
                'name': 'internals', 'data': ['a', 'b', 'c']
            }
        )
        for c in self.c.collections:
            if c['name'] == 'links':
                for d in c['data']:
                    if d['name'] == 'internals':
                        self.assertIn('b', d['data'])


class ScraperTests(unittest.TestCase):
    def setUp(self):
        """ Initialize a Scraper object for testing """
        self.s = Scraper()

    def test_init(self):
        """ Is the testing object of the Scraper type? """
        self.assertIsInstance(self.s, Scraper)
        self.assertIsInstance(self.s.cleaners, dict)

    def test_set_element_type(self):
        """ Does hte set_element_type func modify the object? """
        self.s.set_element_type('a')
        self.assertEqual('a', self.s.type)

    def test_set_attribute(self):
        """ Does the set_attribute func modify the object? """
        self.s.set_attribute('id')
        self.assertEqual('id', self.s.attr)

    def test_set_search_filter(self):
        """ Does the set_search_filter func modify the object? """
        self.s.set_search_filter('nav')
        self.assertEqual('nav', self.s.filter)
        self.s.set_search_filter('^\d')
        self.assertEqual('^\d', self.s.filter)

    def test_sub_scraper(self):
        """ Does creation of sub_scraper populate list of Scraper object? """
        self.s.sub_scraper('body')
        self.assertEqual('body', self.s.sub_scrapers[0].type)

    def test_run(self):
        """ Does running a Scraper with attributes return DOM nodes? """
        self.s = Scraper('input', 'value', 'Google Search')
        self.s.run(urlopen('https://google.com'))
        self.assertEqual(1, len(self.s.raw_data))

    def test_clean_with_attr(self):
        """ Does cleaning a node return formated data? """
        self.s = Scraper('nav', 'id', 'mini-navigation')
        self.s.run(urlopen('http://www.nytimes.com'))
        self.s.clean('attr', 'class')
        self.assertEqual('mini-navigation', self.s.clean_data[0][0]) 
        self.assertIsNot(0, len(self.s.clean_data))
        self.assertIsInstance(self.s.clean_data[0][0], str)  
        with self.assertRaises(AttributeError):
            self.s.clean('blah')

    def test_add_cleaner(self):
        """ Can we add a func to the cleaners list and call it? """
        def custom_cleaner():
            return 1 + 1
        self.s.add_cleaner('custom', custom_cleaner)
        self.assertEqual(2, self.s.cleaners['custom']())


class CleanerTests(unittest.TestCase):
    def setUp(self):
        """ Creates a Scraper object and populates its raw_data w/ HTML """
        self.s = Scraper('a', 'href', re.compile('nytimes'))
        self.s.run(urlopen('http://www.nytimes.com'))

    def test_attr(self):
        """ see also test_clean_with_attr() in ScraperTests """
        pass

    def test_text(self):
        """ Can we extract text strings from node elements? """
        self.s.clean('text')
        self.assertIn('Crossword', self.s.clean_data)


if __name__ == '__main__':
    unittest.main()
