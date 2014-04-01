reporting_structure
===================

The module reporting_sructure defines one method:

**get_structure**(*id*) <br>
Returns the reporting structure of the employee with employee_id = id
as a dictionary of position:employee_id pairs

Further background and notes on the code are in the doc string of auditor.py

####Dependencies
python 2.7

####Example usage:

From the Python interpreter (with auditor.py and employees.py in the current working directory:

```
In [1]: from reporting_structure import get_structure

In [2]: get_structure(47)
Out[2]: {u'ceo': 1, u'director': 5, u'manager': 21, u'vp': 3}
```
