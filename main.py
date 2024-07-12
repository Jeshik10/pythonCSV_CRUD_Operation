from customer import Customer
import controller as c


choice_txt = """
What do you want to do?
1. Add Customer Details.
2. View All Customer.
3. View Customer By ID.
4. Update Customer.
5. Delete Customer.
"""
choice = int(input(choice_txt))
if choice == 1:
  c.add_customer()

elif choice == 2:
   c.view_all_customer() 
   
elif choice == 3:
   print("View Customer By ID")    
   c.view_single_customer()
   
elif choice == 4:
   print("Update Customer")    

elif choice == 5:
   print("Delete Customer")   

else:
   print("Invalid choice!")   
