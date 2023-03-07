from sqlite3 import connect, Cursor


conn = connect('db.sqlite3')
cur = conn.cursor()
cur: Cursor
cur.execute('''
   CREATE TABLE IF NOT EXISTS category(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name VARCHAR(24) NOT NULL UNIQUE
     );
''')

conn.commit()
