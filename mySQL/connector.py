## Author : Sietze Min
## Date : 14-12-2020

import sys
import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "studentroot", ## #################insert correct password here ###########################%#%#%#%#%#%#%#$$#$#$#$#$$$@#@#@
    database = "datacamp"
)
cursor = db.cursor()

# cursor.execute("CREATE DATABASE datacamp")
# cursor.execute("DROP TABLE users")
# cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")

# cursor.execute("ALTER TABLE users DROP id")
# cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")

# query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
# values = ("Hafeez", "hafeez")
# cursor.execute(query, values)
# db.commit()

query = "SELECT * FROM users"
cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)
