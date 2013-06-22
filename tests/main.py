#!/usr/bin/env python

import unittest

import wmflabs


class Test(unittest.TestCase):

    def checkType(self):
        self.assertTrue(hasattr(wmflabs.db.connect, '__call__'))
        self.assertTrue(hasattr(wmflabs.grid.submit, '__call__'))


if __name__ == "__main__":
    unittest.main()
