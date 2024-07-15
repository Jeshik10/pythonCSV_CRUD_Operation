import csv
from customer import Customer

CSV_FILE = 'customers.csv'

def add_customer():
    id = input("Enter customer ID: ")
    name = input("Enter customer name: ")
    phone = input("Enter customer phone: ")
    balance = float(input("Enter customer balance: "))
    
    customer = Customer(id, name, phone, balance)
    
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([customer.id, customer.name, customer.phone, customer.balance])
    
    print("Customer added successfully!")

def view_all_customers():
    try:
        with open(CSV_FILE, 'r') as f:
            reader = csv.reader(f)
            print("All Customers:")
            print("--------------")
            for row in reader:
                customer = Customer(*row)
                customer.display()
            print("--------------")
    except FileNotFoundError:
        print("No customers file found. The customer list is empty.")

def view_single_customer():
    id = input("Enter customer ID to view: ")
    found = False
    try:
        with open(CSV_FILE, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == id:
                    customer = Customer(*row)
                    customer.display()
                    found = True
                    break
        if not found:
            print("Customer not found.")
    except FileNotFoundError:
        print("No customers file found. The customer list is empty.")

def update_customer():
    old_id = input("Enter customer ID to update: ")
    found = False
    updated_customers = []
    try:
        with open(CSV_FILE, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == old_id:
                    print("Current customer details:")
                    Customer(*row).display()
                    
                    new_id = input("Enter new ID (or press enter to keep current): ") or row[0]
                    name = input("Enter new name (or press enter to keep current): ") or row[1]
                    phone = input("Enter new phone (or press enter to keep current): ") or row[2]
                    balance = input("Enter new balance (or press enter to keep current): ") or row[3]
                    updated_customers.append([new_id, name, phone, balance])
                    found = True
                else:
                    updated_customers.append(row)
        
        if found:
            with open(CSV_FILE, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(updated_customers)
            print("Customer updated successfully!")
        else:
            print("Customer not found.")
    except FileNotFoundError:
        print("No customers file found. The customer list is empty.")

def delete_customer():
    id = input("Enter customer ID to delete: ")
    found = False
    updated_customers = []
    try:
        with open(CSV_FILE, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != id:
                    updated_customers.append(row)
                else:
                    found = True
        
        if found:
            with open(CSV_FILE, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(updated_customers)
            print("Customer deleted successfully!")
        else:
            print("Customer not found.")
    except FileNotFoundError:
        print("No customers file found. The customer list is empty.")