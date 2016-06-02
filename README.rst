===============================
XIXI
===============================

A flasky app.

curl -l -H "Content-type: application/json" -X POST -d '{"symbol":"aaa","order_type":"buy","price":100,"amount":100}' http://192.168.33.10:5000/trade.do


curl -i -X POST \
   -H "Content-Type: application/json; indent=4" \
   -d '{
    "symbol": "WSCN",
    "order_type": "buy",
    "price": 100,
    "amount": 100
}' http://192.168.33.10:8000/trade.do

$ curl -i -X POST \
    -H "Content-Type: application/json; indent=4" \
    -d '{
    "symbol": "WSCN",
    "order_id": 1000
}' http://192.168.33.10:5000/cancel_order.do

Quickstart
----------

First, set your app's secret key as an environment variable. For example, example add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export APP_SECRET='something-really-secret'


Then run the following commands to bootstrap your environment.


::

    git clone https://github.com/defbobo/app
    cd app
    pip install -r requirements/dev.txt
    bower install
    python manage.py server

You will see a pretty welcome screen.

Once you have installed your DBMS, run the following to create your app's database tables and perform the initial migration:

::

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server



Deployment
----------

In your production environment, make sure the ``APP_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``db``, and the ``User`` model.


Running Tests
-------------

To run all tests, run ::

    python manage.py test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands:
::

    python manage.py db migrate

This will generate a new migration script. Then run:
::

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``python manage.py db --help``.
