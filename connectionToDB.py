from contextlib import nullcontext
import mysql.connector 
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', database='aqua_analytica', user='root', password='root')
        if conn.is_connected():
            print('Connected to db')
            return conn
        else:
            return nullcontext

    except Error as e:
        print(e)