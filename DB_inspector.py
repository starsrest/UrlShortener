import sqlite3

conn = sqlite3.connect('shortener_database.sqlite3')
cursor = conn.cursor()

tables = ["URLtable"]

for table in tables:
	cursor.execute('SELECT * FROM ' + table)
	print table
	for row in cursor:
		print row

	index = 0
	cursor.execute('SELECT COUNT(*) FROM ' + table)
	for i in cursor:
		index = i[0]
		print 'the table size: %d' % index


