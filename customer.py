class Customer:
    def __init__(self, id, name, phone, balance):
        self.id = id
        self.name = name
        self.phone = phone
        self.balance = float(balance)

    def __str__(self):
        return f"Customer(id={self.id}, name={self.name}, phone={self.phone}, balance=Rs.{self.balance})"

    def display(self):
        print(f"Customer ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Balance: Rs.{self.balance:.2f}")
        print()