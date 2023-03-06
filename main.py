from sqlite3 import connect, Cursor


conn = connect('db.sqlite3')
cur = conn.cursor()
cur: Cursor
cur.execute('''
    CREATE TABLE IF NOT EXISTS tablitsa(        
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name VARCHAR(64) NOT NULL UNIQUE,
         is_published BOOLEAN DEFAULT(false)
     );
''')
conn.commit()
