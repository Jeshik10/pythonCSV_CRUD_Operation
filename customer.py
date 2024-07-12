#Develop a software application for a bank that includes functionalities to add and view customer information. Each customer should have an ID, name, phone number, and balance.

class Customer:
  def __init__(self, id, name, phone, balance):
    self.id = id
    self.name = name
    self.phone = phone
    self.balance = balance
    
  def display_customer(self):
    print(f"Customer id is {self.id}")  
    print(f"Customer name is {self.name}")  
    print(f"Customer phone is {self.phone}")  
    print(f"Customer balance is {self.balance}")  