from Save_All_Contacts import save_all_contacts

def delete_contacts(all_contacts):
    if all_contacts:
        try:
            search_text = input('\nEnter the Contact Name/Phone Number to remove: ').strip().lower()

            contacts_to_delete = []

            for contact in all_contacts:
                if search_text == str(contact['Name']).lower() or search_text == str(contact['Phone_Number']):
                    contacts_to_delete.append(contact)

            if not contacts_to_delete:
                print("\n\tNo contact found with the given name or number.")
                return

            if len(contacts_to_delete) > 1:
                print("\nMultiple contacts found with the search criteria:")
                for idx, contact in enumerate(contacts_to_delete, 1):
                    print(f"{idx}. Name: {contact['Name']} | Phone: {contact['Phone_Number']} | Email: {contact['Email']} | Address: {contact['Address']}")
                
                delete_quiry=input("\nPress 'Y' to delete all or press any key: ").strip().lower()
                if delete_quiry=='y':
                    for c in contacts_to_delete:
                        all_contacts.remove(c)
                    print("\n\tAll matched contacts deleted")
                    save_all_contacts(all_contacts)
                    return
                       
                else:
                    try:
                        delete_index = int(input("\nEnter the number of the contact you want to delete: ")) - 1
                        if delete_index<0 or delete_index>=len(contacts_to_delete):
                            print("Invalid selection. No contact deleted.")
                            return
                        contact_to_delete = contacts_to_delete[delete_index]
                    except ValueError:
                        print("\n\tInvalid input. Enter a valid number.")
                        
            else:
                contact_to_delete = contacts_to_delete[0]

            all_contacts.remove(contact_to_delete)
            print("\n\tContact Deleted Successfully.")
            save_all_contacts(all_contacts)
            
        except ValueError:
            print("\n\tInvalid input. Please enter a valid number when selecting contacts.")
        except Exception as e:
            print("\n\tAn error occurred:", e)
    else:
        print("\n\tNo contacts found.")

