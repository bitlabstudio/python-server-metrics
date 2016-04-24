Python Server Metrics
=====================

A very simple set of methods to collect metrics about your servers

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install python-server-metrics

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/python-server-metrics.git#egg=server_metrics

Usage
-----

Simply import the package and use it anywhere in your python code::

    from server_metrics.memory import get_memory
    from server_metrics.hard_disk import get_disk_usage
    from server_metrics.postgresql import get_database_size
    from server_metrics.cpu import get_cpu_usage
    from server_metrics.memcached import get_memcached_usage

    print get_memory()
    print get_disk_usage('$HOME')
    print get_database_size('my_role', 'my_db')
    print get_cpu_usage('user')
    print get_memcached_usage('~/memcached.sock')


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 python-server-metrics
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
