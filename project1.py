import csv
import cx_Oracle
query='create table empcopy as (select * from emp where 1=2)'
query1='drop table empcopy'
ins_query="insert into empcopy values(:EMPNO,:ENAME,:JOB,:MGR,:HIREDATE,:SAL,:COMM,:DEPTNO)"
file='pro.csv'
records = list()
try:
	file = open('pro.csv')
	#reader=csv.DictReader(file)
	reader=csv.reader(file)
	conn = cx_Oracle.connect('scott/tiger@orcl')
	cursor=conn.cursor()
	next(file)
	for row in reader:
		#print(row)
		if row is not None or row !=():
			#print(len(row))
			row = tuple(row)
			records.append(row)
			value=input('DO you want fetch more record-- YES/NO ')
		if value in ('NO','no'):
			break
		#for abc in records:
	cursor.executemany(ins_query,records)
	conn.commit()
	print('records inserted successfully')
except cx_Oracle.DatabaseError as e:
	print('not connected')
	print(e)
	#cursor.execute(query1)
	if conn:
		conn.rollback