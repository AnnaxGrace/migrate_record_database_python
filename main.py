import psycopg2

f = open("./employees.txt")

records = []

for i in f.readlines():
    records.append(i.split("/ "))

print(records)