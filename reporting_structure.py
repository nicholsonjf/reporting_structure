"""
    Code snippet for Astreya/Google
    ~~~~~

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

"""

import employees, sqlite3
conn = sqlite3.connect('employees.db')
cur = conn.cursor()

columns = 'id', 'position', 'boss'

# query all employee records
sql = """
      SELECT {}
      FROM employees
      """.format(','.join(columns))

# assume 'db' is a connection object that implements the Python DB API 2.0 (PEP 249)
cur.execute(sql)
employee_records = cur.fetchall()

# dictionary of dictionaries in the form {employeenumber: {attribute: value, attribute: value, etc...}}
employees = {}
for i in employee_records:
    employees[i[0]] = {k:v for k,v in zip(columns[1:], i[1:])}

# empty dict to store final data structure
hierarchy = {}

for employee in employees:
	boss = employees[employee]['boss']
	# add empty dict to store superiors of a given employee
	hierarchy[employee] = {}
	# continue if the user has no boss (like the CEO)
	if boss == None:
		continue
	else:
		# recursive while loop to insert superiors until the child's boss == None
		while boss != None:
			boss_position = employees[boss]['position']
			hierarchy[employee][boss_position] = boss
			boss = employees[boss]['boss']

def get_structure(employee_id):
	return hierarchy[employee_id]
