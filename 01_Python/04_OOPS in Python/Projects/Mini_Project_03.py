# Contact Management System

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print("Contact added")

    def search_contact(self, name):
        if name in self.contacts:
            print(name, ":", self.contacts[name])
        else:
            print("Contact not found")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")


cb = ContactBook()
cb.add_contact("Mohit", "9876543210")
cb.search_contact("Mohit")
cb.delete_contact("Mohit")
