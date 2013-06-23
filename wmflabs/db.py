#!/usr/bin/env python
"""
Public domain.

Authors:
 Legoktm, 2013
"""

import os
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

