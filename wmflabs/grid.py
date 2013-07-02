#!/usr/bin/env python
"""
Public domain.

Authors:
 Legoktm, 2013
"""

import os
import pipes
import re
import subprocess

environ = dict(os.environ)
environ['PATH'] = '/bin:/usr/bin:/usr/local/bin'

re_job = re.compile(' (?P<id>\d*?) (?P<prior>\d\.\d*?) (?P<name>.*?)\s*?(?P<user>.*?) (?P<state>.*?)\s*?(?P<date>\d\d/\d\d/\d\d\d\d \d\d:\d\d:\d\d) (?P<queue>.*?)\s*?')


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


def qstat():
    """
    Returns a machine readable output of qstat
    """
    data = []
    output = subprocess.check_output('qstat')
    if not output:
        # No jobs running
        return data
    lines = output.splitlines()[2:]
    for line in lines:
        match = re_job.search(line)
        if match:
            data.append(match.groupdict())
    return data
