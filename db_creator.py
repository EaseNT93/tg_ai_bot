import sys
import mysql.connector
import variables

db = mysql.connector.connect(
      host=variables.host,
      user=variables.user,
      passwd=variables.passwd,
      port=variables.port,
      database=variables.database
    )
cursor = db.cursor()

#cursor.execute("CREATE DATABASE variables.database")
cursor.execute("CREATE TABLE users (first_name VARCHAR(255), last_name VARCHAR(255))")
cursor.execute("ALTER TABLE users ADD COLUMN (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT UNIQUE)")

sql = "INSERT INTO users (first_name, last_name, user_id) VALUES (%s, %s, %s)"
val = ("Ease", "NT", 1)
cursor.execute(sql, val)
db.commit()
