# Import the mysql.connector module, which enables Python to interact with MySQL databases.
import mysql.connector

# Establish a connection to the MySQL database.
mydb = mysql.connector.connect(
  host="localhost",        # Hostname of the MySQL server 
  user="username",         # Username to access the MySQL server 
  password="mypassword",   # Password for the specified username 
  database='databasename'  # Database name 
)

# Create a cursor object to execute SQL queries on the database.
mycursor = mydb.cursor()

# Execute a SQL query to show all databases on the server.

# mycursor.execute("SHOW DATABASES")
# mycursor.execute("SHOW TABLES")
# mycursor.execute("SELECT * FROM student")

# Iterate over the result set returned by the query and print each database name.
# for x in mycursor:
#   print(x)


# how to insert new details into table 

# sql = "INSERT INTO student (id , name, age) VALUES (%s ,%s, %s)"
# val = (8,"John", 45)
# mycursor.execute(sql, val)

# mydb.commit()


# how to delete perticular row from table 

# sql = "DELETE FROM student WHERE id= (%s)"
# val = (5,)
# mycursor.execute(sql,val)
# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")


# how to update the details in table

# sql ="UPDATE  student SET name= (%s), age= (%s) WHERE id = (%s)"
# val = ("Nisar",26,4)
# mycursor.execute(sql,val)
# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")


# Limit AND order

# mycursor.execute("SELECT * FROM student ORDER BY age ASC LIMIT 3")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

