reporting_structure
===================

Create an example employees table and return an employee's reporting structure


Further background and notes on the code are in the doc string of auditor.py

dependencies: python 2.7

Example usage:

From the Python interpreter (with auditor.py and employees.py in the current working directory:

In [1]: from reporting_structure import *

In [2]: get_structure(47)
Out[2]: {u'ceo': 1, u'director': 5, u'manager': 21, u'vp': 3}
