contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"{name} - {details['phone']}")


def search_contact():
    search = input("Enter name or phone number to search: ")

    found = False
    for name, details in contacts.items():
        if search == name or search == details["phone"]:
            print("\nContact Found:")
            print("Name:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            print("Address:", details["address"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    name = input("Enter contact name to update: ")

    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")

        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }

        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


while True:
    print("\n----- CONTACT BOOK MENU -----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice. Try again.")
