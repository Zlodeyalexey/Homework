# from psycopg2 import connect
#
# conn = connect('postgresql://student:password@localhost:5432/homework')
# with conn.cursor() as cursor:
#     with open('category.sql', 'r', encoding='utf-8') as file:
#         cursor.execute(file.read())
#         conn.commit()