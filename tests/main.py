#!/usr/bin/env python

import unittest
import sys
import wmflabs


class Test(unittest.TestCase):

    def testTypes(self):
        self.assertTrue(hasattr(wmflabs.db.connect, '__call__'))
        self.assertTrue(hasattr(wmflabs.db.dbname, '__call__'))
        self.assertTrue(hasattr(wmflabs.grid.submit, '__call__'))
        self.assertTrue(hasattr(wmflabs.grid.qstat, '__call__'))

    def testPy3k(self):
        if sys.version[0] == '3':
            self.assertRaises(NotImplementedError, wmflabs.db.connect, 'enwiki')

    def testDBName(self):
        values = [
            ('en.wikipedia.org', 'enwiki'),
            ('https://en.wikipedia.org', 'enwiki'),
            ('www.wikidata.org', 'wikidatawiki'),
            ('http://commons.wikimedia.org', 'commonswiki'),
            ('en.wikisource.org/wiki/Article', 'enwikisource')
        ]
        for domain, dbname in values:
            self.assertEqual(wmflabs.db.dbname(domain), dbname)


if __name__ == "__main__":
    unittest.main()
