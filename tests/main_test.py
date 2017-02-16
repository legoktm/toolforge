#!/usr/bin/env python

import requests
import unittest
import wmflabs


class MainTest(unittest.TestCase):

    def test_callable(self):
        self.assertTrue(hasattr(wmflabs.connect, '__call__'))
        self.assertTrue(hasattr(wmflabs.dbname, '__call__'))

    def test_dbname(self):
        values = [
            ('en.wikipedia.org', 'enwiki'),
            ('https://en.wikipedia.org', 'enwiki'),
            ('www.wikidata.org', 'wikidatawiki'),
            ('http://commons.wikimedia.org', 'commonswiki'),
            ('en.wikisource.org/wiki/Article', 'enwikisource')
        ]
        for domain, dbname in values:
            self.assertEqual(wmflabs.dbname(domain), dbname)

    def test_set_user_agent(self):
        orig = requests.utils.default_user_agent
        wmflabs.set_user_agent('mycooltool')
        self.assertEqual(
            requests.get('https://httpbin.org/user-agent').json(),
            {'user-agent': 'mycooltool (https://tools.wmflabs.org/mycooltool; '
             'tools.mycooltool@tools.wmflabs.org) python-requests/2.13.0'}
        )
        requests.utils.default_user_agent = orig


if __name__ == "__main__":
    unittest.main()
