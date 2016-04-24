"""Utilities for getting memory related metrics."""
import psutil


def get_memory_usage(user=None):
    """
    Returns a three-tupel with memory usage for the given user.

    The result contains::

        (total memory, largest process' memory, largest process name)

    :param user: String representing the user. If `None`, the total size of
      all processes for all users will be returned.

    """
    total = 0
    largest_process = 0
    largest_process_name = None
    for p in psutil.process_iter():
        p_user = p.username()
        if user is None or p_user == user:
            try:
                process_memory = p.memory_info()[0]
            except psutil.AccessDenied:
                continue
            total += process_memory
            if process_memory > largest_process:
                largest_process = process_memory
                largest_process_name = p.name()
    return total, largest_process, largest_process_name
