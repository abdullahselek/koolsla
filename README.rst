.. raw:: html

   <div align="center">

.. image:: https://raw.githubusercontent.com/abdullahselek/koolsla/master/resources/logo.png

.. raw:: html

   </div>

.. raw:: html

   <h1 align="center">

koolsla

.. raw:: html

   </h1>

.. raw:: html

   <h4 align="center">

Food recommendation tool with Machine learning

.. raw:: html

   </h4>

.. image:: https://img.shields.io/pypi/v/koolsla.svg
    :target: https://pypi.python.org/pypi/koolsla/

.. image:: https://img.shields.io/pypi/pyversions/koolsla.svg
    :target: https://pypi.org/project/koolsla

.. image:: https://codecov.io/gh/abdullahselek/koolsla/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/abdullahselek/koolsla

+--------------------------------------------------------------------------+------------------------------------------------------------------------------------+
|                                Linux                                     |                                       Windows                                      |
+==========================================================================+====================================================================================+
| .. image:: https://travis-ci.org/abdullahselek/koolsla.svg?branch=master | .. image:: https://ci.appveyor.com/api/projects/status/l5bt8yw7n35cvsov?svg=true   |
|   :target: https://travis-ci.org/abdullahselek/koolsla                   |    :target: https://ci.appveyor.com/project/abdullahselek/koolsla                  |
+--------------------------------------------------------------------------+------------------------------------------------------------------------------------+

Description
===========

koolsla (`Coleslaw <https://en.wikipedia.org/wiki/Coleslaw>`_) is a recommendation tool based on Machine Learning with contents.
Developed with the power of `tf-idf <https://en.wikipedia.org/wiki/Tf%E2%80%93idf>`_ and `Cosine Similarity <https://en.wikipedia.org/wiki/Cosine_similarity>`_.

The user gives a natural number that corresponds to the ID of a unique dish name. Through `tf-idf` the plot summaries of 424508 different dishes that reside in the dataset, are analyzed and vectorized. 
Set of dishes (number set by user) is chosen as recommendations based on their `cosine similarity` with the vectorized input.

koolsla is mainly an educational project.

Installation
============

You can install koolsla using::

    $ pip install koolsla

Getting the code
================

The code is hosted at https://github.com/abdullahselek/koolsla

Check out the latest development version anonymously with::

    $ git clone git://github.com/abdullahselek/koolsla.git
    $ cd koolsla

To install test dependencies, run either::

    $ pip install -Ur requirements.testing.txt

Running Tests
=============

The test suite can be run against a single Python version which requires ``pip install pytest`` and optionally ``pip install pytest-cov``
(these are included if you have installed dependencies from ``requirements.testing.txt``)

To run the unit tests with a single Python version::

    $ py.test -v

To also run code coverage::

    $ py.test --cov=koolsla

To run the unit tests against a set of Python versions::

    $ tox

Sample Usage
============

Import recommender::

    from koolsla import recommender

Getting recommendations with dish id and recommendation count::

    // Returns dictionary of tuples [(dish_id_1, similarity_ratio1), (dish_id_2, similarity_ratio2), (dish_id_3, similarity_ratio3)]
    recommendatons = recommender.recommend(82, 3)
