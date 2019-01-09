#!/usr/bin/env python

import os
import requests
import unittest
import unittest.mock

import toolforge


class MainTest(unittest.TestCase):

    def test_callable(self):
        self.assertTrue(hasattr(toolforge.connect, '__call__'))
        self.assertTrue(hasattr(toolforge.dbname, '__call__'))

    def test_dbname(self):
        values = [
            ('en.wikipedia.org', 'enwiki'),
            ('https://en.wikipedia.org', 'enwiki'),
            ('www.wikidata.org', 'wikidatawiki'),
            ('http://commons.wikimedia.org', 'commonswiki'),
            ('en.wikisource.org/wiki/Article', 'enwikisource')
        ]
        for domain, dbname in values:
            self.assertEqual(toolforge.dbname(domain), dbname)

    def test_set_user_agent(self):
        orig = requests.utils.default_user_agent
        requests.utils.default_user_agent = lambda: 'python-requests/2.13.0'
        expected = 'mycooltool (https://tools.wmflabs.org/mycooltool; ' +\
                   'tools.mycooltool@tools.wmflabs.org) python-requests/2.13.0'
        ret = toolforge.set_user_agent('mycooltool')
        self.assertEqual(ret, expected)
        self.assertEqual(
            requests.get('https://httpbin.org/user-agent').json(),
            {'user-agent': expected}
        )
        requests.utils.default_user_agent = orig

    def test_connect(self):
        tests = [
            (['enwiki_p'], {
                'database': 'enwiki_p',
                'host': 'enwiki.web.db.svc.eqiad.wmflabs',
            }),
            (['enwiki'], {
                'database': 'enwiki_p',
                'host': 'enwiki.web.db.svc.eqiad.wmflabs',
            }),
            (['enwiki', 'analytics'], {
                'database': 'enwiki_p',
                'host': 'enwiki.analytics.db.svc.eqiad.wmflabs',
            }),
            (['enwiki_p', 'labsdb'], {
                'database': 'enwiki_p',
                'host': 'enwiki.labsdb',
            }),
        ]
        common_expects = {
            'read_default_file': os.path.expanduser("~/replica.my.cnf"),
            'charset': 'utf8mb4',
        }

        for args, expects in tests:
            with unittest.mock.patch('toolforge._connect') as mm:
                mm.return_value = None
                exp = common_expects.copy()
                exp.update(expects)

                conn = toolforge.connect(*args)

                assert conn is None
                mm.assert_called_once_with(**exp)


if __name__ == "__main__":
    unittest.main()
