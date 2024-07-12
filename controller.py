from customer import Customer
import csv

all_customer = []

def add_customer():
  print("Adding Customer")
  c = Customer(id=0, name="", phone=0, balance=0)
  c.id = int(input("Enter Customer ID: "))
  c.name = input("Enter Customer name: ")
  c.phone = int(input("Enter Customer phone_no.: "))
  c.balance = float(input("Enter Customer balance: "))
  f = open('customer.csv','a')
  f.write(f"{c.id}, {c.name}, {c.phone}, {c.balance}\n")
  f.close()
  print(f"Details of {c.name} Added Successfully!")

def view_all_customer():
  f = open('customer.csv','r')
  print("All Customers are:\n--------------")
  print(f.read())
  print("--------------")

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


def delete_customer(id):
  print(f"Delete Customer {id}")

  def update_customer(id):
    print(f"update customer {id}")

  def search_customer(first_name):
    print("searching customer")