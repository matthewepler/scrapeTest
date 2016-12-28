#!/usr/bin/env python3

import unittest

# import main
from controller import Controller


class MainTests(unittest.TestCase):
    def test_one_plus_one(self):
        assert 1 + 1 == 2


class ControllerTests(unittest.TestCase):
    def setUp(self):
        """ Create an instance of Controller """
        self.c = Controller(
            url='http://www.google.com/#',
        )

    def test_instance(self):
        """ Is the instance of the class type we expect? """
        self.assertIsInstance(self.c, Controller)

    def test_not_equal(self):
        """ Are instances unique in memory? """
        self.assertNotEqual(self.c, Controller(
            url='http://www.google.com/#',
            params={
                'q': 'hamlet',
            }
        ))

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
        self.c.create_collection('titles')
        self.assertEqual('titles', self.c.collections[-1]['name'])
        self.assertEqual(len(self.c.collections[-1]['data']), 0)


class ScraperTests(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()
