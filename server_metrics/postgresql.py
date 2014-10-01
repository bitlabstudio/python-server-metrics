"""Utilities for getting postgreSQL related metrics."""
import commands


def get_database_size(db_user, db_name):
    """
    Returns the total size for the given database role and name.

    :param db_user: String representing the database role.
    :param db_name: String representing the database name.

    """
    cmd = 'psql -U {0} -c "select pg_database_size(\'{1}\');"'.format(
        db_user, db_name)
    total = commands.getoutput(cmd).split()[2]
    total = int(total)
