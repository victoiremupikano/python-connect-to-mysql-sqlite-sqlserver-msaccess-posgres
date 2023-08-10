# !pip install PyMySQL
# Now we will import that package
import pymysql

db = pymysql.connect(host="localhost", user="root", password="0000", port=3306)
# you have cursor instance here
cursor = db.cursor()
# on print la version
cursor.execute("select version()")
# on recuper les bases de donnes qui sont
cursor.execute("show databases")
data = cursor.fetchall()
# on affcihe le nombre des bd
print("Le nombre total des bases de donnees :")
print(len(data))
print("La liste des bases de donnees :")
for i in data:
    print(i)
    
# connection a la base de donne specifique
dbd = pymysql.connect(host="localhost", user="root", password="0000", port=3306, database="sakila")
cursor = dbd.cursor()
# on recuper les bases de donnes qui sont
cursor.execute("show tables")
data = cursor.fetchall()
print("La liste des tables de 'sakila' :")
for i in data:
    print(i)
    
    