from Save_All_Contacts import save_all_contacts

def add_contacts(all_contact):
    
    try:
        name = input("\nName: ").strip()
        if not name:
            print("\n\tName can't be empty")
            return all_contact
        
        phone_number = input("Phone Number: ").strip()
        if phone_number and (not phone_number.isdigit()):
            print("\nInvalid phone number. Please enter numeric values only.")
            return all_contact
        for contact in all_contact:
            if contact["Phone_Number"] == phone_number:
                print("\nA contact with this phone number already exists.")
                return all_contact
        
        email = input("Email: ").strip()
        if email and ("@" not in email or "." not in email):
            print("\nInvalid email address. Please enter a valid email.")
            return all_contact
        
        if not phone_number and not email:
            print("\nYou must provide a phone number or an email to add a contact")
            return all_contact
        
        valid_blood_groups = {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"}
        blood_group=input("Blood Group: ").strip().upper()
        if blood_group and blood_group not in valid_blood_groups:
            print("\nInvalid blood group. Please enter a valid blood group.")
            return all_contact
        
        address = input("Address: ").strip()

        contact = {
            "Name": name,
            "Phone_Number": phone_number,
            "Email": email,
            "Blood_Group": blood_group,
            "Address": address,
        }

        all_contact.append(contact)
        print("\n\tContact Added Successfully!")
        save_all_contacts(all_contact)

    except Exception as e:
        print("\nAn error occured while adding contact.")

