import cx_Oracle

con = cx_Oracle.connect('scott/tiger@127.0.0.1:1521/xe')
print('Oracle Database version: {}'.format(con.version))

cur = con.cursor()
cur.execute('SELECT * FROM EMP ORDER BY EMPNO')

for result in cur:
    print(result)

cur.close()
con.close()
