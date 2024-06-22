import sqlite3

# connection object
conn = sqlite3.connect('INSTRUCTOR.db')

# cursor object
cursor_obj = conn.cursor()

# Drop the table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")

# Creating table
table = """Create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME Varchar(20), LNAME Varchar(20), CITY Varchar(20), CCODE CHAR(2));"""

cursor_obj.execute(table)

# Insert data to table
data = '''INSERT into INSTRUCTOR values(1,'Ankit','Sharma','RANCHI','RNC')'''
cursor_obj.execute(data)

# Insert multiple data to table
multi_data = '''insert into INSTRUCTOR values (2, 'Aditya', 'Sharma', 'RANCHI', 'RNC'), (3, 'Ankita', 'Sharma', 'RANCHI', 'RNC')'''
cursor_obj.execute(multi_data)

# Fetch data from table
query = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(query)

print("Print all data")
output = cursor_obj.fetchall()
for row in output:
    print(row)

# Fetch specific number of rows from table
query = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(query)

print("Specific counts of rows")
count = 2
specfic_output = cursor_obj.fetchmany(count)
for row in specfic_output:
    print(row)


# Update data in table
update_data = '''UPDATE INSTRUCTOR SET CITY='BANGALORE' where FNAME="Ankit"'''
cursor_obj.execute(update_data)

print("Print updated data")
query1 = '''SELECT * FROM INSTRUCTOR where FNAME="Ankit"'''
cursor_obj.execute(query1)
new_data = cursor_obj.fetchall()
for row in new_data:
    print(row)
conn.close()
