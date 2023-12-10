contact = {}

def display_contact():
   print()
   print("Name\t\tContact Number")
   print("----\t\t--------------")
   for i in contact:
      print(i,"\t\t",contact[i])
   print()
   print()

for key in contact:
   print("{}\t\t{}".format(key,contact.get(key)))
                            
while True:
   choice = int(input(" 1. Add new contact \n 2. Search contact \n 3. Display Contact \n 4. Edit contact \n 5. Delete Contact \n 6. Exit \n\n Enter your Choice: "))
   if choice == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        contact[name] = phone
        print("Added Succesfully")
        # print(contact[name])
   elif choice == 2:
      print()
      search_name = input("Enter the contact name: ")
      if search_name in contact:
         print(search_name+"\'s contact number is", contact[search_name])
         print()
      else:
         print("Name is not found in contact book")
         print()
   elif choice == 3:
      if contact=={}:
         print("Empty Contact Book")
         print()
      else:
         display_contact()
   elif choice == 4:
      print()
      edit_contact = input("Enter the contact to be Edited: ")
      if edit_contact in contact :
           phone = input("Enter Mobile Number: ")
           contact[edit_contact]=phone
           print("Contact Updated")
           display_contact()
           
      else:
           print("Name Is not Found in contact Book")
   elif choice == 5:
      del_contact = input("Enter the contact to be deleted: ")     
      if del_contact in contact:
         confirm = input("Do you want do delete this contact y/n: ")
         if confirm == 'y' or confirm == 'Y' :
            contact.pop(del_contact)
         display_contact()
      else:
         print("Name is not found in contact book")
   else:
      break
