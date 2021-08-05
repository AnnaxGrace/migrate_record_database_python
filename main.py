import psycopg2

f = open("./employees.txt")

records = []

for i in f.readlines():
    records.append(i.split("/ "))

print(records)

try:
    connection = psycopg2.connect(database = "staff", user = "anna", password = "python", host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("Yeah no")

else:
    print("Connection was successful")

cursor = connection.cursor()

try:
    for i in records:
        cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) values (%s, %s, %s, %s, %s, %s, %s);",(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

except psycopg2.Error as err:
    print("error sorry :(")

else: 
    print("Records inserted successfully")

connection.commit()

connection.close()