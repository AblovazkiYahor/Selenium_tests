import mysql.connector as mysql

db_test = mysql.connect(host="localhost",
                    user="root",
                    passwd="Genius150199",
                    database = 'test_db')

cursor = db_test.cursor()
#cursor.execute("DESC orders")

#cursor.execute("DROP TABLE orders")
#cursor.execute("CREATE TABLE orders (ord_no INT, purch_amt FLOAT, ord_date DATE, customer_id INT, salesman_id INT)")
#cursor.execute("DESC orders")
#print(cursor.fetchall())
#columns = "INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (%s, %s, %s, %s, %s)"
#values = [
#     (70001, 150.5, "2012-10-05", 3005, 5002),
#     (70009, 270.65, "2012-09-10", 3001, 5005),
#     ("70002", "65.26", "2012-10-05", "3002", "5001"),
#     ("70004", "110.5", "2012-08-17", "3009", "5003"),
#     ("70007", "948.5", "2012-09-10", "3005", "5002"),
#     ("70005", "2400.6", "2012-07-27", "3007", "5001"),
#     ("70008", "5760.0", "2012-09-10", "3002", "5001"),
#     ("70010", "1983.43", "2012-10-10", "3004", "5006"),
#     ("70003", "2480.4", "2012-10-10", "3009", "5003"),
#     ("70012", "250.45", "2012-06-27", "3008", "5002")
#
# ]
# cursor.executemany(columns, values)
# db_test.commit()
# print(cursor.rowcount, "records inserted")
# print(cursor.fetchall())

#response = "SELECT ord_no, purch_amt, ord_date FROM orders WHERE salesman_id = 5002"
#cursor.execute(response)
#print(cursor.fetchall())

#salesman_id = "SELECT DISTINCT salesman_id FROM orders"
#cursor.execute(salesman_id)
#print(cursor.fetchall())

# order_by = "SELECT DISTINCT ord_date, customer_id, ord_no, purch_amt FROM orders ORDER BY ord_date ASC"
# cursor.execute(order_by)
# print(cursor.fetchall())

# between = "SELECT DISTINCT ord_no FROM orders WHERE ord_no BETWEEN 70001 AND 70007 ORDER BY ord_no ASC"
# cursor.execute(between)
# print(cursor.fetchall())