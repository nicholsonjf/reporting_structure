reporting_structure
===================

####Background
At E*Trade, one of the features of the application I developed is to take data describing an
employee's access privileges to an application, and send it to the appropriate person in the
business for review and approval. It's not a terribly exciting problem to solve, but critical
for regulatory compliance.

There are different workflow rules, depending on the application. For instance, user access to App X
must be approved by the user's manager or above, whereas access to App Y need be reviewed by at least
a director (in the same reporting line as the user).

Thus, before routing any of the tens of thousands of records that come through the application each
quarter, I have to know who to route it to.

To solve this problem, I used a bit of recursion to create a nested dictionary and a function that returns
the reporting structure of any employee in that dict. Thus, no matter the workflow rule, I can access the id of
the right approver.

####Methods
The module reporting_sructure defines one method:

**get_structure**(*id*) <br>
Returns the reporting structure of the employee with employee_id = id
as a dictionary of position:employee_id pairs

####Dependencies
python 2.7

####Example usage:
From the Python interpreter (with auditor.py and employees.py in the current working directory:

```
In [1]: from reporting_structure import get_structure

In [2]: get_structure(47)
Out[2]: {u'ceo': 1, u'director': 5, u'manager': 21, u'vp': 3}
```
