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
                    print(f"{idx}. Name: {contact['Name']} | Phone: {contact['Phone_Number']}")
                delete_index = int(input("\nEnter the number of the contact you want to delete: ")) - 1
                contact_to_delete = contacts_to_delete[delete_index]
            else:
                contact_to_delete = contacts_to_delete[0]

            all_contacts.remove(contact_to_delete)
            save_all_contacts(all_contacts)
            print("\n\tContact Deleted Successfully.")

        except ValueError:
            print("\n\tInvalid input. Please enter a valid number when selecting contacts.")
        except Exception as e:
            print("\n\tAn error occurred:", e)
    else:
        print("\n\tNo contacts found.")

