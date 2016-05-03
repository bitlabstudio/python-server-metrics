"""Utilities for getting postgreSQL related metrics."""
try:
    from subprocess import getoutput
except ImportError:
    from commands import getoutput


def get_database_size(db_user, db_name, localhost=False):
    """
    Returns the total size for the given database role and name.

    :param db_user: String representing the database role.
    :param db_name: String representing the database name.

    """
    localhost_part = ''
    if localhost:
        localhost_part = '-h localhost '
    cmd = 'psql {0}-U {1} -c "select pg_database_size(\'{2}\');"'.format(
        localhost_part, db_user, db_name)
    total = getoutput(cmd).split()[2]
    return int(total)
