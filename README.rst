=============================
robot_backend
=============================

.. image:: https://badge.fury.io/py/robot_backend.svg
    :target: https://badge.fury.io/py/robot_backend

.. image:: https://travis-ci.org/leonardoo/robot_backend.svg?branch=master
    :target: https://travis-ci.org/leonardoo/robot_backend

.. image:: https://codecov.io/gh/leonardoo/robot_backend/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/leonardoo/robot_backend

Your project description goes here

Documentation
-------------

The full documentation is at https://robot_backend.readthedocs.io.

Quickstart
----------

Install robot_backend::

    pip install robot_backend

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'robot_backend.apps.RobotBackendConfig',
        ...
    )

Add robot_backend's URL patterns:

.. code-block:: python

    from robot_backend import urls as robot_backend_urls


    urlpatterns = [
        ...
        url(r'^', include(robot_backend_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
