import json

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        contact = {'name': name, 'phone_number': phone_number, 'email': email}
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact['name']} - {contact['phone_number']} - {contact['email']}")

    def edit_contact(self, index, name, phone_number, email):
        if 1 <= index <= len(self.contacts):
            self.contacts[index - 1] = {'name': name, 'phone_number': phone_number, 'email': email}
            print(f"Contact '{name}' updated successfully!")
        else:
            print("Invalid index. No contact updated.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(f"Contact '{deleted_contact['name']}' deleted successfully!")
        else:
            print("Invalid index. No contact deleted.")

    def save_to_file(self, filename='contacts.json'):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)
        print(f"Contacts saved to {filename}.")

    def load_from_file(self, filename='contacts.json'):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
            print(f"Contacts loaded from {filename}.")
        except FileNotFoundError:
            print(f"No previous contacts found. Starting with an empty list.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("6. Load Contacts from File")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone_number, email)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            index = int(input("Enter the index of the contact you want to edit: "))
            name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            contact_manager.edit_contact(index, name, phone_number, email)

        elif choice == '4':
            index = int(input("Enter the index of the contact you want to delete: "))
            contact_manager.delete_contact(index)

        elif choice == '5':
            contact_manager.save_to_file()

        elif choice == '6':
            contact_manager.load_from_file()

        elif choice == '7':
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
