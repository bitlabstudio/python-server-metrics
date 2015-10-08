"""Utilities for getting postgreSQL related metrics."""
import commands


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
    total = commands.getoutput(cmd).split()[2]
    total = int(total)
    return total
