# This module is responsible to create the database and its tables
import sqlite3

def init_sqlite():
    # this function will be called by tha main application. It creates the database and the data stores 
    conn = sqlite3.connect('database/database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor() # cursor: interador que permite navegar e manipular os registros do bd.
    
    try: 
        with open('database/createtables.sql', 'r') as slqitescript:
            create_tables_script = slqitescript.read()
        
        cursor.executescript(create_tables_script)
        print('SQLite script executed correctly')
        return conn
    except sqlite3.Error as error:
        print('Error while executing sqlite scripts', error)

def finish_sqlite(conn):
    if conn:
        conn.close()
        print('SQLite connection is closed')



# execute: lê e executa comandos SQL puro diretamente no bd. (SINGLE SQL STATEMENT)
# executescript: (MULTIPLE SQL STATEMENTS) o commit está incluso