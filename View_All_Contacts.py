def view_all_contacts(all_contacts):
    """Displays all contacts in a formatted manner."""
    if not all_contacts:
        print("\n\tNo contacts found.")
        return

    print("\nContact List:")
    print("-" * 40)

    for contact in all_contacts:
        try:
            print(f"\n\tName: {contact['Name']}")
            print(f"\tPhone Number: {contact['Phone_Number']}")
            print(f"\tEmail: {contact['Email']}")
            print(f"\tBlood Group: {contact['Blood_Group']}")
            print(f"\tAddress: {contact['Address']}")
            print("-" * 40)
        except KeyError as e:
            print(f"\nError: Missing key {e} in contact data.")
            continue
