#!/usr/bin/env python
"""
Public domain.

Authors:
 Legoktm, 2013
"""

import os
import pipes
import subprocess

environ = os.environ
environ['PATH'] = '/bin:/usr/bin:/usr/local/bin'


def submit(command, **kwargs):
    """
    Example:
     submit('python script.py', N='script', mem='500M')
    """
    cmd = '/usr/local/bin/jsub '
    for kw in kwargs:
        cmd += '-{0} {1} '.format(kw, pipes.quote(kwargs[kw]))
    cmd += command
    output = subprocess.check_output(cmd,
                                     stderr=subprocess.STDOUT,
                                     shell=True,
                                     env=environ,
                                     )
    return output.split(' ')[2]
