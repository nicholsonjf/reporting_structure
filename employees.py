import sqlite3
from random import choice

# create and connect to employees database
sqlite3.connect('employees.db')
conn = sqlite3.connect('employees.db')
cur = conn.cursor()

# create employees table
cur.execute("CREATE TABLE IF NOT EXISTS employees (id integer, position text, boss integer)")
conn.commit()

# create employees as lists of tuples
ceo = [(1, 'ceo', None)]

veeps = []
for i in range(2,4):
	veeps.append((i, 'vp', 1))

directors = []
for i in range(4, 15):
	directors.append((i, 'director', choice([i for i in range(2,4)])))

managers = []
for i in range(15,45):
	managers.append((i, 'manager', choice([i for i in range(4,15)])))

associates = []
for i in range(45, 146):
	associates.append((i, 'associate', choice([i for i in range(15, 45)])))

# insert employees into newly created table
for position in ceo, veeps, directors, managers, associates:
	for employee in position:
		cur.execute("INSERT INTO employees VALUES (?,?,?)", employee)
conn.commit()

