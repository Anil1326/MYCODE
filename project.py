import csv
import cx_Oracle
query='select * from emp'
file='pro.csv'
fieldnames=['EMPNO','ENAME','JOB','MGR','HIREDATE','SAL','COMM','DEPTNO']
data_list=list()
try:
	file=open('pro.csv','w')
	writer=csv.writer(file,fieldnames)
	conn = cx_Oracle.connect('scott/tiger@orcl')
	cursor=conn.cursor()
	cursor.execute(query)
	row=cursor.fetchone()
	while row is not None:
		#print(row)
		#writer.writerow(row)
		data_list.append(row)
		row=cursor.fetchone()
		value=input('DO you want fetch more record-- YES/NO ')
		if value in ('NO','no'):
			row = None
	for row in data_list:
		writer.writerow(row)
	print('successfully connected')
	print(data_list)
except cx_Oracle.DatabaseError as e:
        if conn != None:
           conn.rollback()
           print('there is problm:',e)
