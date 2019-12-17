import time
import sys
import warnings


warnings.filterwarnings('ignore')

# Loading animation
animation = ". |/-\\"

print("\n")
for i in range(30):
    time.sleep(0.1)
    if i < 28:
        sys.stdout.write("\r \tLOADING..." + animation[i % len(animation)])
        sys.stdout.flush()
    else:
        sys.stdout.write("\r \tLOADED. ")

print("\n")

myAddressBook = {}


# Displays the main menu of address book
def menu():
    print('''
=== Address Book ===
[a] Add Contact
[b] Print Contact
[c] Update Contact
[d] Delete Contact
[e] Search Contact
[f] Exit
''')


# Function to add contact
def addcontact():
    name = input('Enter your name: ')
    for x in myAddressBook:
        if x.lower() == name.lower():
            time.sleep(1)
            print('Name is already in address book.')
            break
    else:
        address = input('Enter your address: ')
        phone = input('Enter your mobile number: ')
        email = input('Enter your email: ')
        birthday = input('Enter your birthday: <mm/dd/yyyy> ')
        print(name, 'has been added.')
        myAddressBook[name] = name, phone, address, email, birthday


# Function to print all contacts
def printallcontact():
    for x in myAddressBook:
        print(myAddressBook[x])


# Function to print birthday sorted by date
def printbirthday():
    sorted_myaddressBook = sorted(myAddressBook, key=myAddressBook.__getitem__)
    for k in sorted_myaddressBook:
        print("{} : {}".format(k, myAddressBook[k]))


# Function to update contact in address book
def updatecontact():
    name = input('Enter name to update contact: ')
    if name in myAddressBook:
        if name.lower() == name.lower():
            address = input('Address: ')
            phone = input('Mobile number: ')
            email = input('Email: ')
            birthday = input('Birthday: ')
            myAddressBook[name] = name, phone, address, email, birthday
            print(name, 'has been updated.')
    else:
        print(name, 'Contact not found.')


# Function to delete contact in address book
def deletecontact():
    name = input("Enter contact to be deleted: ")
    if name in myAddressBook:
        del myAddressBook[name]
        print(name, 'was successfully deleted.')
    else:
        print(name, "was not found in address book.")


# Function to search for a name and print the person's phone number
def searchcontact():
    name = input('Search[name]: ')
    if name in myAddressBook:
        print(myAddressBook[name])
    else:
        print(name, 'was not found')


# Condition when specifying the letter of choice
while True:
    menu()
    choice = input('Enter letter of choice: ')
    if choice == 'a':
        addcontact()
    elif choice == 'b':
        print('''
            a. Print all contacts
            b. Print birthdays for each month

            ''')
        choice2 = input('Enter choice: ')
        if choice2 == 'a':
            printallcontact()
        elif choice2 == 'b':
            printbirthday()
    elif choice == 'c':
        updatecontact()
    elif choice == 'd':
        deletecontact()
    elif choice == 'e':
        searchcontact()
    elif choice == 'f':
        print('Program will now exit. ')
        exit()
