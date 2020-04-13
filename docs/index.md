# koolsla

[![Build Status](https://github.com/abdullahselek/koolsla/workflows/koolsla%20ci/badge.svg)](https://github.com/abdullahselek/koolsla/actions)
[![pypi](https://img.shields.io/pypi/v/koolsla.svg)](https://pypi.python.org/pypi/koolsla/)
[![pyversions](https://img.shields.io/pypi/pyversions/koolsla.svg)](https://pypi.org/project/koolsla)
[![codecov](https://codecov.io/gh/abdullahselek/koolsla/branch/master/graph/badge.svg)](https://codecov.io/gh/abdullahselek/koolsla)


**Documentation**: <a href="https://koolsla.abdullahselek.com" target="_blank">https://koolsla.abdullahselek.com</a>

**Source Code**: <a href="https://github.com/abdullahselek/koolsla" target="_blank">https://github.com/abdullahselek/koolsla</a>

koolsla <a href="https://en.wikipedia.org/wiki/Coleslaw" target="_blank">Coleslaw</a> is a recommendation tool based on Machine Learning with contents.
Developed with the power of <a href="https://en.wikipedia.org/wiki/Tf%E2%80%93idf">tf-idf</a> and <a href="https://en.wikipedia.org/wiki/Cosine_similarity">Cosine Similarity</a>

The user gives a natural number that corresponds to the ID of a unique dish name. Through `tf-idf` the plot summaries of 424508 different dishes that reside in the dataset, are analyzed and vectorized. 
Set of dishes (number set by user) is chosen as recommendations based on their `cosine similarity` with the vectorized input.

koolsla is mainly an educational project.
