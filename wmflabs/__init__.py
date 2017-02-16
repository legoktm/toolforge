#!/usr/bin/env python
"""
Small library for common tasks on Wikimedia Labs
Copyright (C) 2013, 2017 Kunal Mehta <legoktm@member.fsf.org>

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


def connect(dbname, **kwargs):
    """
    Get a database connection for the
    specified wiki
    :param dbname: Database name
    :param kwargs: For pymysql.connect
    :return: pymysql connection
    """
    if dbname.endswith('_p'):
        dbname = dbname[:-2]
    if dbname == 'meta':
        host = 'enwiki.labsdb'
    else:
        host = dbname + ".labsdb"
    return pymysql.connect(
        database=dbname + '_p',
        host=host,
        read_default_file=os.path.expanduser("~/replica.my.cnf"),
        charset='utf8mb4',
        **kwargs
    )


def dbname(domain):
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


@functools.lru_cache()
def _fetch_sitematrix():
    params = {'action': 'sitematrix', 'format': 'json'}
    headers = {'User-agent': 'https://wikitech.wikimedia.org/wiki/User:Legoktm/wmflib'}
    r = requests.get('https://meta.wikimedia.org/w/api.php', params=params, headers=headers)
    r.raise_for_status()
    return r.json()
