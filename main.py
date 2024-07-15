import controller as c

menu = """
Customer Management System
1. Add Customer
2. View All Customers
3. View Customer by ID
4. Update Customer
5. Delete Customer
6. Exit
"""

while True:
    print(menu)
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        c.add_customer()
    elif choice == '2':
        c.view_all_customers()
    elif choice == '3':
        c.view_single_customer()
    elif choice == '4':
        c.update_customer()
    elif choice == '5':
        c.delete_customer()
    elif choice == '6':
        print("Thank you for using the Customer Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    
    input("\nPress Enter to continue...")