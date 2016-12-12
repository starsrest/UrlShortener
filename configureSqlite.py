import sqlite3

def createDB():
	con = sqlite3.connect("shortener_database.sqlite3")
	cur = con.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS URLtable (tableindex INT, shorturl TEXT, longurl TEXT, PRIMARY KEY (tableindex))')
	con.commit()

def insertDB():
	con = sqlite3.connect("shortener_database.sqlite3")
	cur = con.cursor()

	#insert 3 movies
	cur.execute("""INSERT INTO URLtable VALUES(10, 'http://ascdas', 'casdascewaefea')""")

	cur.execute("""INSERT INTO URLtable VALUES(11, 'http://aseeec', '@$#@%4333')""")

	cur.execute("""INSERT INTO URLtable VALUES(12, 'http://ooeeqec', '%#$%@GGfffe')""")	
	con.commit()

if __name__ == "__main__":
	createDB()
	# insertDB()