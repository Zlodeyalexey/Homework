from psycopg2 import connect

conn = connect('postgresql://zlodey:password@localhost:5432/belhard')
with conn.cursor() as cursor:
    with open('users.sql', 'r', encoding='utf-8') as file:
        cursor.execute(file.read())
        conn.commit()
