'''
Difference between Connection and Cursor.
Conn - It is the connection object to the database.
Conn - It is the iterator object over a specific resultset.
'''
import psycopg2
from psycopg2.extras import RealDictCursor

def connect():
    try:
        conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='pg123',cursor_factory=RealDictCursor)
        print('Connected to Database.')
        return conn
    except Exception as error:
        print('Failed to connect.')
        print("Error",error)

def sqlquery(sql:str,params=None):
    try:        
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql) if not params else cursor.execute(sql,params) 
        data = cursor.fetchall()
        rowcount = cursor.rowcount
        cursor.close()
        conn.commit()
        conn.close()
        print('Successfully executed SQL - ',sql)
        print('Row Count - ',rowcount)
        return(data)
    except Exception as error:
        print('Failed to execute SQL - ',sql)
        print('Error',error)
        
