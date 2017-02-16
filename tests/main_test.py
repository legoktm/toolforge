#!/usr/bin/env python

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


if __name__ == "__main__":
    unittest.main()
