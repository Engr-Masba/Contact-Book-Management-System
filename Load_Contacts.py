import csv

def load_contacts(file_name):
    contacts = []
    try:
        with open(file_name, "r") as file:
            content = csv.DictReader(file)
            for row in content:
                contacts.append(row)
    except FileNotFoundError:
        print(f"\nWarning: {file_name} not found. Starting with an empty contact list.")
    except Exception as e:
        print(f"\nError loading contacts: {e}")
    return contacts