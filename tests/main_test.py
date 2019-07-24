#!/usr/bin/env python

import os
import pytest
import requests

import toolforge


class TestMain:

    def test_callable(self):
        assert hasattr(toolforge.connect, '__call__')
        assert hasattr(toolforge.dbname, '__call__')

    @pytest.mark.parametrize('domain,dbname', [
        ('en.wikipedia.org', 'enwiki'),
        ('https://en.wikipedia.org', 'enwiki'),
        ('www.wikidata.org', 'wikidatawiki'),
        ('http://commons.wikimedia.org', 'commonswiki'),
        ('en.wikisource.org/wiki/Article', 'enwikisource')
    ])
    def test_dbname(self, domain, dbname):
        assert toolforge.dbname(domain) == dbname

    def test_set_user_agent(self):
        orig = requests.utils.default_user_agent
        requests.utils.default_user_agent = lambda: 'python-requests/2.13.0'
        expected = 'mycooltool (https://tools.wmflabs.org/mycooltool; ' +\
                   'tools.mycooltool@tools.wmflabs.org) python-requests/2.13.0'
        ret = toolforge.set_user_agent('mycooltool')
        assert ret == expected
        assert requests.get('https://httpbin.org/user-agent').json() == \
            {'user-agent': expected}
        requests.utils.default_user_agent = orig

    @pytest.mark.parametrize('args, expects', [
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
    ])
    def test_connect(self, mocker, args, expects):
        common_expects = {
            'read_default_file': os.path.expanduser("~/replica.my.cnf"),
            'charset': 'utf8mb4',
        }

        mm = mocker.patch('toolforge._connect')
        mm.return_value = None
        exp = common_expects.copy()
        exp.update(expects)

        conn = toolforge.connect(*args)

        assert conn is None
        mm.assert_called_once_with(**exp)
