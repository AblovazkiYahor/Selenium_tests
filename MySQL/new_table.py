import mysql.connector as mysql

db_test = mysql.connect(host="localhost",
                    user="root",
                    passwd="Genius150199",
                    database = 'test_db')

cursor = db_test.cursor()
#cursor.execute("CREATE DATABASE test_db")
#cursor.execute("SHOW DATABASES")
#cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")
#cursor.execute("ALTER TABLE users ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")
#cursor.execute("SHOW TABLES")
#cursor.execute("DESC users")
#print(cursor.fetchall())
'''query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
values = [
    ("Peter", "peter"),
    ("Amy", "amy"),
    ("Michael", "michael"),
    ("Hennah", "hennah")
]

cursor.executemany(query, values)
db_test.commit()
print(cursor.rowcount, "records inserted")'''
query = "SELECT * FROM users"
cursor.execute(query)
print(cursor.fetchall())


