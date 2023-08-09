# pip install pyodbc

import pyodbc
 
 
msa_drivers = [x for x in pyodbc.drivers() if 'ACCESS' in x.upper()]
print(f'MS-Access Drivers : {msa_drivers}')
 
try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Victoire\Documents\db.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected To Database")
    
    # insertion dans la table
    cursor = conn.cursor()
 
    myuser = (
 
        (1, 'data', 'data@gmail.com'),
        (2, 'python', 'python@gnail.com'),
        (3, 'java', 'java@gmail.com'),
     )
 
    cursor.executemany('INSERT INTO users VALUES (?,?,?)', myuser)
    conn.commit()
    print('Data Inserted')
except pyodbc.Error as e:
    print("Error in Connection", e)
