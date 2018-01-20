PostgresDB Backup
========

CLI for backing up remote PostgesSQL databases locally 

Pre-requisites
---------------

::

    $ chmod u+x install_docker_and_db.sh  && ./install_docker_and_db

Preparing for Development
--------------------------

1. Ensure ``pip``, and ``pipenv`` are installed.
2. Clone the repo: ``https://github.com/ayoubensalem/PostgresBackup``
3. Fetch development dependencies : ``make install``


Usage
------

Pass in a full database URL, the storage driver, and destination.


Local Example w/ local path:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql



Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make























