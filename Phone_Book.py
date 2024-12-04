import Add_Contact
import View_All_Contacts
import Delete_Contact
import Load_Contacts
import Search_Contact


file_name = "All_Contacts.csv"
All_Contacts = Load_Contacts.load_contacts(file_name)

while True:
    print("\nWelcome to Contact Book Management System\n")
    print("\t1. Search contact")
    print("\t2. View All Contacts")
    print("\t3. Add Contact")
    print("\t4. Delete Contact")
    print("\t5. Reset Contact List")
    print("\t0. Exit")

    menu = input("\nSelect any number: ")

    if menu=="1":
        Search_Contact.search_contacts(All_Contacts)
    elif menu == "2":
        View_All_Contacts.view_all_contacts(All_Contacts)
    elif menu == "3":
        Add_Contact.add_contacts(All_Contacts)
    elif menu == "4":
        Delete_Contact.delete_contacts(All_Contacts)
    elif menu == "5":
        confirm = input("\nAre you sure you want to reset all contacts? (yes/no): ").strip().lower()
        if confirm == "yes":
            All_Contacts.clear()
            print("\nYour phonebook is now empty.")
    elif menu == "0":
        print("\nThanks for using Contact Book Management System.\n")
        break
            
    else:
        print("\nChoose a valid number.")


