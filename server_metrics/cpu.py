"""Utilities for getting CPU related metrics."""
import decimal
import commands


def get_cpu_usage(user=None):
    """
    Returns the total CPU usage for all available cores.

    :param user: If given, returns only the total CPU usage of all processes
      for the given user.

    """
    user_flag = ' '
    if user is not None:
        user_flag = ' -u {0} '.format(user)
    cmd = "ps%s-o pcpu | awk '{sum+=$1} END {print sum}'" % user_flag
    output = commands.getoutput(cmd)
    total = decimal.Decimal(output)
    return total
