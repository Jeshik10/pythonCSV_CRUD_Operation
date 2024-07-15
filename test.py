from customer import Customer
import csv
import controller as c

all_customer = []

def view_single_customer():
  print("View single Customer")

  id = int(input("Enter customer id: "))

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

    
def convert_customer_to_csv(listofcustomer):
  file = open("customer.csv",'w')
  file.write("")
  file.close()

  for c in listofcustomer:
    f = open("customer.csv",'a')
    f.write(f"{c.id}, {c.name}, {c.phone}, {c.balance}\n")
    f.close()

# def convert_csv_to_customer_list():
#   with open('customer.csv','r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#       c = Customer(id=row[0], name=row[1], phone=row[2], balance=float(row[3]))
#       all_customer.append(c)   
#       return all_customer

# all_cust = convert_csv_to_customer_list()
# print(all_cust)