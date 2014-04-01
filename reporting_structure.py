import employees, sqlite3

# connect to sqlite DB created by the employees.py script
conn = sqlite3.connect('employees.db')
cur = conn.cursor()

columns = 'id', 'position', 'boss'

# query all employee records
sql = """
      SELECT {}
      FROM employees
      """.format(','.join(columns))
cur.execute(sql)

# store employee records as a list of tuples
employee_records = cur.fetchall()

# dictionary of dictionaries to quickly access each employee record by id
employees = {}
for i in employee_records:
    employees[i[0]] = {k:v for k,v in zip(columns[1:], i[1:])}

# empty dict to store the desired heirarchical data structure
hierarchy = {}

for employee in employees:
	boss = employees[employee]['boss']
	# add empty dict to store the reporting line for a given employee
	hierarchy[employee] = {}
	# continue if the user has no boss (like the CEO)
	if boss == None:
		continue
	else:
		# recursive while loop to insert superiors until boss == None
		while boss != None:
			boss_position = employees[boss]['position']
			hierarchy[employee][boss_position] = boss
			boss = employees[boss]['boss']

def get_structure(employee_id):
	return hierarchy[employee_id]
