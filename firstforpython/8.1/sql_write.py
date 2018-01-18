import sqlite3 
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()

curs.execute('INSERT INTO zoo VALUES("DUCK", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("SANGUCK", 2, 1000.0)')
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000.0))

curs.execute('SELECT * FROM zoo')

rows = curs.fetchall()
print(rows)