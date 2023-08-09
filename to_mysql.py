# !pip install PyMySQL
# Now we will import that package
import pymysql

db = pymysql.connect(host="localhost", user="root", password="toor", port=3310)
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
