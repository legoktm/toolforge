#!/usr/bin/env python

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
        orig = requests.__version__
        requests.__version__ = '2.13.0'
        expected = 'mycooltool (https://mycooltool.toolforge.org/; ' +\
                   'tools.mycooltool@tools.wmflabs.org) python-requests/2.13.0'
        ret = toolforge.set_user_agent('mycooltool')
        assert ret == expected
        # Allow calling set_user_agent twice (see #14)
        ret2 = toolforge.set_user_agent('mycooltool')
        assert ret2 == expected
        assert requests.get('https://httpbin.org/user-agent').json() == \
            {'user-agent': expected}
        requests.__version__ = orig

    @pytest.mark.parametrize('args, expects', [
        (['enwiki_p'], {
            'database': 'enwiki_p',
            'host': 'enwiki.web.db.svc.wikimedia.cloud',
        }),
        (['enwiki'], {
            'database': 'enwiki_p',
            'host': 'enwiki.web.db.svc.wikimedia.cloud',
        }),
        (['enwiki', 'analytics'], {
            'database': 'enwiki_p',
            'host': 'enwiki.analytics.db.svc.wikimedia.cloud',
        }),
    ])
    def test_connect(self, mocker, args, expects):
        self._assert_connect(mocker, toolforge.connect, args, expects)

    def _assert_connect(self, mocker, func, args, expect):
        """Mock toolforge._connect and assert it is called as expected.

        :param func: Function to call after mocking toolforge._connect
        :param args: Arguments for calling func
        :param expect: Dict of expected arguments to toolforge._connect
        """
        mm = mocker.patch('toolforge._connect')
        mm.return_value = None
        conn = func(*args)
        assert conn is None
        mm.assert_called_once_with(**expect)

    @pytest.mark.parametrize('args,expects', [
        (['s12345__foo'], {
            'database': 's12345__foo',
            'host': 'tools.db.svc.eqiad.wmflabs',
        }),
        (['s12345__foo_p'], {
            'database': 's12345__foo_p',
            'host': 'tools.db.svc.eqiad.wmflabs',
        }),
    ])
    def test_toolsdb(self, mocker, args, expects):
        self._assert_connect(mocker, toolforge.toolsdb, args, expects)
