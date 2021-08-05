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