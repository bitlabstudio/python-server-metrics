"""Utilities for getting memcached related metrics."""
import os

import commands


def get_memcached_usage(socket=None):
    """
    Returns memcached statistics.

    :param socket: Path to memcached's socket file.

    """
    cmd = 'echo \'stats\' | nc -U {0}'.format(socket)
    output = commands.getoutput(cmd)
    curr_items = None
    bytes_ = None

    rows = output.split('\n')[:-1]
    for row in rows:
        row = row.split()
        if row[1] == 'curr_items':
            curr_items = int(row[2])
        if row[1] == 'bytes':
            bytes_ = int(row[2])
    return (bytes_, curr_items)
