"""Utilities for getting hard disk related metrics."""
import subprocess


def get_disk_usage(path):
    """
    Returns the allocated disk space for the given path in bytes.

    :param path: String representing the path as it would be given to the `du`
      command. Best to give an absolute path here.

    """
    cmd = 'du -sh --block-size=1 {0}'.format(path)
    total = subprocess.getoutput(cmd).split()[0]
    return int(total)
