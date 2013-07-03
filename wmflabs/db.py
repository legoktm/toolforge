#!/usr/bin/env python
"""
Public domain.

Authors:
 Legoktm, 2013
"""

import os
import requests
import sys


def connect(dbname):
    if sys.version[0] == '3':
        raise NotImplementedError
    if dbname.endswith('_p'):
        dbname = dbname[:-2]
    import oursql
    return oursql.connect(db=dbname + '_p',
                          host=dbname + ".labsdb",
                          read_default_file=os.path.expanduser("~/replica.my.cnf"),
                          charset=None,
                          use_unicode=False,
                          )

def dbname(domain):
    # Function to figure out the dbname.
    # TODO: Cache these results

    # First, lets normalize the name.
    if domain.startswith(('http://', 'https://')):
        domain = domain.replace('http://', '', 1).replace('https://', '', 1)
    if '/' in domain:
        domain = domain.split('/', 1)[0]

    domain = 'http://' + domain  # May need to change when goes HTTPS-only
    params = {'action': 'sitematrix', 'format': 'json'}
    headers = {'User-agent': 'https://wikitech.wikimedia.org/wiki/User:Legoktm/wmflib'}
    r = requests.get('https://meta.wikimedia.org/w/api.php', params=params, headers=headers)
    data = r.json()['sitematrix']
    for num in data:
        if num.isdigit():
            for site in data[num]['site']:
                if site['url'] == domain:
                    return site['dbname']
        elif num == 'specials':
            for special in data[num]:
                if special['url'] == domain:
                    return special['dbname']
