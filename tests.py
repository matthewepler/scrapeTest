#!/usr/bin/env python3

import unittest

# import main
from controller import Controller


class MainTests(unittest.TestCase):
    def test_one_plus_one(self):
        assert 1 + 1 == 2


class ControllerTests(unittest.TestCase):
    def setUp(self):
        """Create an instance of Controller for testing. No params argument."""
        self.c = Controller(
            url='http://www.google.com/#',
        )

    def test_instance(self):
        self.assertIsInstance(self.c, Controller)

    def test_not_equal(self):
        self.assertNotEqual(self.c, Controller(
            url='http://www.google.com/#',
            params={
                'q': 'hamlet',
            }
        ))

    def test_update_url(self):
        self.c.update_url('http://yahoo.com')
        self.assertIn('yahoo', self.c.base_url)

    def test_update_params(self):
        self.c.update_params({
            'name': 'Matthew',
            'job': 'developer'
        })
        self.assertEqual('developer', self.c.base_params['job'])

if __name__ == '__main__':
    unittest.main()
