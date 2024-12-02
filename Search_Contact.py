def search_contacts(all_contacts):
    if all_contacts:
        try:
            search_text= input('\nEnter Name/Contact Number/Email/Blood Group/Address Contact Number: ').strip()
            
            contact_found = False
            print("\nContact List:")
            print("-" * 40)

            for contact in all_contacts:
                if (search_text.lower() == str(contact['Name']).lower() or
                    search_text == str(contact['Phone_Number']) or
                    search_text.lower() == str(contact['Email']).lower() or
                    search_text.lower() == str(contact['Blood_Group']).lower() or
                    search_text.lower() in str(contact['Address']).lower()):
                    
                    print(f"\n\tName: {contact['Name']}")
                    print(f"\tPhone Number: {contact['Phone_Number']}")
                    print(f"\tEmail: {contact['Email']}")
                    print(f"\tBlood Group: {contact['Blood_Group']}")
                    print(f"\tAddress: {contact['Address']}")
                    print("-" * 40)
                    contact_found=True
            if not contact_found:
                print("\n\tThere is no such contact in your contact list")
        except Exception as e:
            print("\n\tAn error occurred:", e)
    else:
        print("\n\tYour Phone Book is Empty")
        
