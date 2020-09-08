import sqlite3
#connection obj that represent our database with in memory database to create a file called employee database file
conn = sqlite3.connect(':memory:') #so it can start from scratch, if you dont want to keep deleting a database over and over..you add :memory:
#to create a cursor to start running sql command
c = conn.cursor()

#c.execute("""CREATE TABLE employees (
            #first text,
            #last text,
            #pay integer
            #)""")

#to start adding data into the database

c.execute("INSERT INTO employees VALUES ('Corey', 'real', 500)")

conn.commit()

c.execute("SELECT * FROM employees WHERE last='real'")

print (c.fetchall())
          
conn.commit()

conn.close()
