phone_book = {}

def add_contact(name, number):
    phone_book[name] = number
    print(f"Contact {name} added successfuly")

def lookup_contact(name):
    return phone_book.get(name, "Contact not found.")

def display_contacts():
    if not phone_book:
        print("The phone book is empty")
    else:
        for name, number in phone_book.items():
            print(f"Name: {name} Number {number}")

while True:
    print("\n--- Phone Book Menu ---")
    print("1. Add Contact")
    print("2. Look Up Contact")
    print("3. Display All Contacts")
    print("4. Quit")

    users_answer  = input("Choose an option (1-4): ")

    if users_answer == "1":
        name = input("Enter the contact's name: ")
        number = input("Enter the contact's phone number: ")
        add_contact(name, number)
    elif users_answer == "2":
        name = input("What is the contact's name: ")
        print(lookup_contact(name))
    elif users_answer == "3":
        display_contacts()
    elif users_answer == "4":
        print("Exiting phone book, hope you had a good day!")
        break
    else:
        print("ERROR! DOES NOT COMPUTE! PLEASE TRY AGAIN IN 7 YEARS")