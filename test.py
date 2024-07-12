import csv
from customer import Customer

id = int(input("Enter customer id: "))
all_customer = []

with open('customer.csv','r') as file:
  csv_reader = csv.reader(file)
  for row in csv_reader:
    #print(f"{row} hello")
    c = Customer(id=row[0], name=row[1], phone=row[2], balance=float(row[3]))
    all_customer.append(c)

customer = None
for c in all_customer:
  if int(c.id) == id:
    record_found = True
    customer = c
    break

if customer:
  print("Record is Found")
  customer.display_customer()
else:
  print("Customer Id not found!")  


