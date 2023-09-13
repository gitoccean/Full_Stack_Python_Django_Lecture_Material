contact_list = {}
while True:
     print("Address Book")
     print("1: Add a new contact in Address Book.")
     print("2: Display all contacts in Address Book")
     print("3: Quit the program")

     choice = int(input("Press the number to perform function."))

     if choice == 1:

             name = str(input("Enter the name of a employee:  "))
             phone_number = int(input("Enter the phone number of employee:  "))
             address = str(input("Enter the address of employee:  "))


             contact_list[name] = {"Phone Number" : phone_number , "Address" : address}
             print(f"Contact '{name}' has been successfully added into your Address Book. ")



     elif choice == 2:
         if not contact_list:
             print("Address Book is empty. ")

         else:
             print("Address Book ")
             for name, info in contact_list.items():
                 print(f" Name: {name}, Phone Number: {info['Phone Number']}, Address: {info['Address']}")
                 print()

     elif choice == 3:
         print("Thanks for visiting our Employee's Address Book.")
         break

     else:
         print("Invalid "
               "Input! please choose from given functions.")




