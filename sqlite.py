## SqLite Data base
####################################
import sqlite3
## connect to the datbase
conn =sqlite3.connect('customer.db')
## create a cursor
c = conn.cursor()
##c.execute(""" CREATE TABLE customer (
          ###first_name text,
          ##last_name text,
        ##  email text
      ##    )""")
##c.execute("""insert into customer
  ##        values('Prajin','Khatiwada','prajinkhatiwada@gmail.com')""")
c.execute("select * from customer")
items=c.fetchall()
for item in items:
    print(item[0] + " " +item[1])
print("data added to the table....")
### commit our changes  
conn.commit()






#### close database coonection
conn.close()