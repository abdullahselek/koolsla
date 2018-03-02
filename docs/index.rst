.. koolsla documentation master file, created by

Contents:
 
Welcome to koolsla's documentation!
==================================
**Food recommendation tool with Machine learning.**

Author: Abdullah Selek

Contents:

.. toctree::
   :maxdepth: 1

   installation.rst
   koolsla.rst

Introduction
------------

koolsla (`Coleslaw <https://en.wikipedia.org/wiki/Coleslaw>`_) is a recommendation tool based on Machine Learning with contents.
Developed with the power of `tf-idf <https://en.wikipedia.org/wiki/Tf%E2%80%93idf>`_ and `Cosine Similarity <https://en.wikipedia.org/wiki/Cosine_similarity>`_.

The user gives a natural number that corresponds to the ID of a unique dish name. Through `tf-idf` the plot summaries of 424508 different dishes that reside in the dataset, are analyzed and vectorized. 
Set of dishes (number set by user) is chosen as recommendations based on their `cosine similarity` with the vectorized input.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`