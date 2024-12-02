from Save_All_Contacts import save_all_contacts

def add_contacts(all_contact):
    name = input("\nName: ").strip()
    phone_number = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    blood_group=input("Blood Group: ").strip()
    address = input("Address: ").strip()

    if phone_number and (not phone_number.isdigit() or not (10 < len(phone_number) < 15)):
        print("\nInvalid phone number. Please enter numeric values only.")
        return all_contact

    if "@" not in email or "." not in email:
        print("\nInvalid email address. Please enter a valid email.")
        return all_contact

    for contact in all_contact:
        if contact["Phone_Number"] == phone_number:
            print("\nA contact with this phone number already exists.")
            return all_contact

    contact = {
        "Name": name,
        "Phone_Number": phone_number,
        "Email": email,
        "Blood_Group": blood_group,
        "Address": address,
    }

    all_contact.append(contact)
    save_all_contacts(all_contact)

    print("\nContact Added Successfully!")

