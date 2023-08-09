# pip install pypyodbc
import pypyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'LAPTOP-43VNSJFS'
DATABASE_NAME = 'DB_NAME'

# uid=<username>;
# pwd=<password>;

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={{{SERVER_NAME}}};
    DATABASE={{{DATABASE_NAME}}};
    Trust_Connection=ues;    
"""

# on ouvre la connection
conn = odbc.connect(connection_string)
# on affiche la connection
print(conn)