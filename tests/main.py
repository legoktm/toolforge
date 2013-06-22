#!/usr/bin/env python

import unittest
import sys
import wmflabs


class Test(unittest.TestCase):

    def testTypes(self):
        self.assertTrue(hasattr(wmflabs.db.connect, '__call__'))
        self.assertTrue(hasattr(wmflabs.grid.submit, '__call__'))

    def testPy3k(self):
        if sys.version[0] == '3':
            self.assertRaises(NotImplementedError, wmflabs.db.connect, 'enwiki')


if __name__ == "__main__":
    unittest.main()
