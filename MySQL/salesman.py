import mysql.connector as mysql

db_test = mysql.connect(host="localhost",
                    user="root",
                    passwd="Genius150199",
                    database = 'test_db')

cursor = db_test.cursor()

#cursor.execute("CREATE TABLE salesman (name VARCHAR(255), city VARCHAR(255), commission FLOAT, grade INT(100))")
#cursor.execute("CREATE TABLE salesman ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")
cursor.execute("DESC salesman")
#cursor.execute("SHOW TABLES")
print(cursor.fetchall())
columns = "INSERT INTO salesman (name, city, commission, grade) VALUES (%s, %s, %s, %s)"
values = [
    ("James Hoog", "New York", "0.15", "100"),
    ("Nail Knite", "Paris", "0.13", "200"),
    ("Pit Alex", "London", "0.11", "150"),
    ("Mc Lyon", "Paris", "0.14", "50"),
    ("Paul Adam", "Rome", "0.13", "200"),
    ("Lauson Hen", "San Jose", "0.12", "300")

]

cursor.executemany(columns, values)
db_test.commit()
print(cursor.rowcount, "records inserted")
print(cursor.fetchall())





