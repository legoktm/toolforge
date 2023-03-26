#!/usr/bin/env python
"""
Small library for common tasks on Wikimedia Toolforge
Copyright (C) 2013, 2017 Kunal Mehta <legoktm@debian.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import functools
import os
import pymysql
import requests
from typing import Optional


def connect(dbname: str, cluster: str = 'web', **kwargs) -> pymysql.connections.Connection:
    """
    Get a database connection for the
    specified wiki
    :param dbname: Database name
    :param cluster: Database cluster (analytics or web)
    :param kwargs: For pymysql.connect
    :return: pymysql connection
    """
    if cluster not in ['analytics', 'web']:
        raise ValueError('"cluster" must be one of: "analytics", "web"')

    domain = '{}.db.svc.wikimedia.cloud'.format(cluster)

    if dbname.endswith('_p'):
        dbname = dbname[:-2]

    if dbname == 'meta':
        host = 's7.{}'.format(domain)
    else:
        host = '{}.{}'.format(dbname, domain)
    host = kwargs.pop('host', host)

    return _connect(
        database=dbname + '_p',
        host=host,
        **kwargs
    )


def _connect(*args, **kwargs) -> pymysql.connections.Connection:
    """Wraper for pymysql.connect to make testing easier."""
    kw = {
        'read_default_file': os.path.expanduser("~/replica.my.cnf"),
        'charset': 'utf8mb4',
    }
    kw.update(kwargs)
    return pymysql.connect(*args, **kw)  # type: ignore


def toolsdb(dbname: str, **kwargs) -> pymysql.connections.Connection:
    """Connect to a database hosted on the toolsdb cluster.

    :param dbname: Database name
    :param kwargs: For pymysql.connect
    :return: pymysql connection
    """
    return _connect(
        database=dbname,
        host='tools.db.svc.eqiad.wmflabs',
        **kwargs
    )


def dbname(domain: str) -> str:
    """
    Convert a domain/URL into its database name
    """
    # First, lets normalize the name.
    if domain.startswith(('http://', 'https://')):
        domain = domain.replace('http://', '', 1).replace('https://', '', 1)
    if '/' in domain:
        domain = domain.split('/', 1)[0]

    domain = 'https://' + domain
    data = _fetch_sitematrix()['sitematrix']
    for num in data:
        if num.isdigit():
            for site in data[num]['site']:
                if site['url'] == domain:
                    return site['dbname']
        elif num == 'specials':
            for special in data[num]:
                if special['url'] == domain:
                    return special['dbname']

    raise ValueError('Unable to find database name')


@functools.lru_cache()
def _fetch_sitematrix():
    params = {'action': 'sitematrix', 'format': 'json'}
    headers = {'User-agent': 'https://wikitech.wikimedia.org/wiki/User:Legoktm/toolforge_library'}
    r = requests.get('https://meta.wikimedia.org/w/api.php', params=params, headers=headers)
    r.raise_for_status()
    return r.json()


def set_user_agent(tool: str, url: Optional[str] = None, email: Optional[str] = None) -> str:
    """
    Set the default requests user-agent to a better
    one in accordance with
    <https://meta.wikimedia.org/wiki/User-Agent_policy>
    :param tool: Toolforge tool name
    :param url: Optional URL
    :param email: Optional email
    :return New User-agent value
    """
    if url is None:
        url = 'https://{}.toolforge.org/'.format(tool)
    if email is None:
        email = 'tools.{}@tools.wmflabs.org'.format(tool)

    ua = '{} ({}; {}) python-requests/{}'.format(tool, url, email, requests.__version__)
    requests.utils.default_user_agent = lambda *args, **kwargs: ua
    return ua
