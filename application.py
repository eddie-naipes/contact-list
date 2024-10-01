class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = False

    def __str__(self):
        return f'{self.name} - {self.phone} -  {self.email} - {self.favorite}'

    def change_status_favorite(self):
        self.favorite = not self.favorite



contacts: list = []


def create_contact(name, phone, email):
    contact = Contact(name, phone, email)
    contacts.append(contact)

def show_all_contacts():
    for contact in contacts:
        print(contact)


def delete_contact(name):
    for contact in contacts:
        if contact.name == name:
            contacts.remove(contact)
            break

def update_contact(name, phone, email):

    for contact in contacts:
        if contact.name == name:
            contact.phone = phone
            contact.email = email
            break

def favorite_contact(name):
    for contact in contacts:
        if contact.name == name:
            contact.change_status_favorite()
            break



def show_menu():
    print('1 - Create contact')
    print('2 - Show all contacts')
    print('3 - Update contact')
    print('4 - Delete contact')
    print('5 - Favorite contact')
    print('0 - Exit')


while True:
    show_menu()
    option = int(input('Choose an option: '))

    if option == 1:
        name = input('Name: ')
        phone = input('Phone: ')
        email = input('Email: ')
        create_contact(name, phone, email)
    elif option == 2:
        show_all_contacts()
    elif option == 3:
        name = input('Name: ')
        phone = input('Phone: ')
        email = input('Email: ')
        update_contact(name, phone, email)
    elif option == 4:
        name = input('Name: ')
        delete_contact(name)
    elif option == 5:
        name = input('Name: ')
        favorite_contact(name)
    elif option == 0:
        break
    else:
        print('Invalid option')