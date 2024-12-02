from Save_All_Contacts import save_all_contacts

def update_contacts(all_contacts):
    """Updates a contact in the contact list."""
    if not all_contacts:
        print("\nNo contacts found.")
        return

    search_text = input("\nEnter the contact name or contact number to update: ").strip().lower()
    contact_found = False

    for contact in all_contacts:

        if (search_text.lower() == str(contact['Name']).lower() or search_text == str(contact['Phone_Number'])):
            contact_found = True

            print("\nCurrent Contact Details:")
            print(f"Name: {contact['Name']}")
            print(f"Phone Number: {contact['Phone_Number']}")
            print(f"Email: {contact['Email']}")
            print(f"Blood Group: {contact['Blood_Group']}")
            print(f"Address: {contact['Address']}")

            name = input("\nNew Name (Leave blank to keep current): ").strip() or contact['Name']
            phone_number = input("New Phone Number (Leave blank to keep current): ").strip() or contact['Phone_Number']
            email = input("New Email (Leave blank to keep current): ").strip() or contact['Email']
            blood_group=input("New Blood Group (Leave blank to keep current): ").strip() or contact['Blood_Group']
            address = input("New Address (Leave blank to keep current): ").strip() or contact['Address']

            if phone_number and (not phone_number.isdigit() or not (10 < len(phone_number) < 15)):
                print("\nInvalid phone number. It must be between 11 and 14 digits. Update canceled.")
                return

            contact['Name'] = name
            contact['Phone_Number'] = phone_number
            contact['Email'] = email
            contact['Blood_Group']=blood_group
            contact['Address'] = address

            save_all_contacts(all_contacts)
            print("\nContact Updated Successfully!")
            break

    if not contact_found:
        print("\nNo contact found with the given name or phone number.")
    
    

