#!/usr/bin/env python
"""
Public domain.

Authors:
 Legoktm, 2013
"""

import os
import oursql


def connect(dbname):
    return oursql.connect(db=dbname + '_p',
                          host=dbname + ".labsdb",
                          read_default_file=os.path.expanduser("~/replica.my.cnf"),
                          charset=None,
                          use_unicode=False,
    )
