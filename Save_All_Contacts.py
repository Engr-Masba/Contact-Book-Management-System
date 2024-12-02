import csv

def save_all_contacts(all_contacts, file_name="All_Contacts.csv"):
    """Saves all contacts to a CSV file."""
    if all_contacts:
        try:
            with open(file_name, "w", newline="") as file:
                fieldnames = all_contacts[0].keys()
                content = csv.DictWriter(file, fieldnames=fieldnames)
                content.writeheader()
                content.writerows(all_contacts)

            print("\nContacts saved successfully to", file_name)
        except Exception as e:
            print("\nAn error occurred while saving contacts:", e)
            
    else:
        print("\nNo contacts to save.")


