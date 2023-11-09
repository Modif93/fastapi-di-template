FastAPI + SQLAlchemy + Dependency Injector Template
==================================================

This is a Template of Spring Like package structure from Dependency Injector Examples.

from : `Dependency Injector <https://github.com/ets-labs/python-dependency-injector>`_ 's
 `FastAPI + SQLAlchemy + Dependency Injector Example <https://github.com/ets-labs/python-dependency-injector/tree/master/examples/miniapps/fastapi-sqlalchemy>_`

Run
---

Build the Docker image:

.. code-block:: bash

   docker-compose build

Run the docker-compose environment:

.. code-block:: bash

    docker-compose up

The output should be something like:

.. code-block::

   Starting fastapi-sqlalchemy_webapp_1 ... done
   Attaching to fastapi-sqlalchemy_webapp_1
   webapp_1  | 2022-02-04 22:07:19,804 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
   webapp_1  | 2022-02-04 22:07:19,804 INFO sqlalchemy.engine.base.Engine ()
   webapp_1  | 2022-02-04 22:07:19,804 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
   webapp_1  | 2022-02-04 22:07:19,804 INFO sqlalchemy.engine.base.Engine ()
   webapp_1  | 2022-02-04 22:07:19,805 INFO sqlalchemy.engine.base.Engine PRAGMA main.table_info("users")
   webapp_1  | 2022-02-04 22:07:19,805 INFO sqlalchemy.engine.base.Engine ()
   webapp_1  | 2022-02-04 22:07:19,808 INFO sqlalchemy.engine.base.Engine PRAGMA temp.table_info("users")
   webapp_1  | 2022-02-04 22:07:19,808 INFO sqlalchemy.engine.base.Engine ()
   webapp_1  | 2022-02-04 22:07:19,809 INFO sqlalchemy.engine.base.Engine
   webapp_1  | CREATE TABLE users (
   webapp_1  | 	id INTEGER NOT NULL,
   webapp_1  | 	email VARCHAR,
   webapp_1  | 	hashed_password VARCHAR,
   webapp_1  | 	is_active BOOLEAN,
   webapp_1  | 	PRIMARY KEY (id),
   webapp_1  | 	UNIQUE (email),
   webapp_1  | 	CHECK (is_active IN (0, 1))
   webapp_1  | )
   webapp_1  |
   webapp_1  |
   webapp_1  | 2022-02-04 22:07:19,810 INFO sqlalchemy.engine.base.Engine ()
   webapp_1  | 2022-02-04 22:07:19,821 INFO sqlalchemy.engine.base.Engine COMMIT
   webapp_1  | INFO:     Started server process [8]
   webapp_1  | INFO:     Waiting for application startup.
   webapp_1  | INFO:     Application startup complete.
   webapp_1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

After that visit http://127.0.0.1:8000/docs in your browser.

Test
----

This application comes with the unit tests.

To run the tests do:

.. code-block:: bash

   docker-compose run --rm webapp py.test webapp/test/user.py --cov=webapp

