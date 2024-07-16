class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }

    def view_contacts(self):
        for name, details in self.contacts.items():
            print(f"{name}: {details['phone']} | {details['email']} | {details['address']}")

    def search_contact(self, query):
        for name, details in self.contacts.items():
            if query.lower() in name.lower() or query in details['phone']:
                print(f"{name}: {details['phone']} | {details['email']} | {details['address']}")

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            print(f"{name} updated successfully.")
        else:
            print(f"{name} not found in contacts.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} deleted successfully.")
        else:
            print(f"{name} not found in contacts.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            query = input("Enter search query (name or phone): ")
            contact_book.search_contact(query)
        elif choice == '4':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_book.update_contact(name, phone, email, address)
        elif choice == '5':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()


