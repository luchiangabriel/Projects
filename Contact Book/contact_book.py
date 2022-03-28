
import mysql.connector

print("""
Python: "Let's work togheter, MySQL!"
MySQL: "Sure thing"\n
Let's authenticate!
""")


def db_user():
    user = str(input("Enter the name of the user: ")).strip()
    print(f"You are authenticated with username: {user}!\n")
    return user


def db_password():
    password = str(input("Enter the password of the user: ")).strip()
    print(f"You are authenticated with password: {password}!\n")
    return password


def db_database():
    database = str(input("Enter the name for the database: ")).strip()
    print(f"You are using now {database} database!")
    return database


user_db = db_user()
pass_db = db_password()
database_db = db_database()

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user=user_db,
    password=pass_db,
    database=f"{database_db}"
    )


def options():
    print("""
               1. Show all contacts
  |---------|  2. Add a contact
  | Options |  3. Search a contact
  |---------|  4. Edit a contact
               5. Delete a contact
              ---------------------------
               0. Close the contact book 
            """)
    option = int(input("Enter option: "))
    while option not in [0, 1, 2, 3, 4, 5]:
        print("Invalid option entered!")
        options()
    else:
        return option


def show_contacts():
    db_cursor = mydb.cursor()
    db_cursor.execute("SELECT * FROM contact")
    print('\n{0:20}{1:30}'.format('NAME', 'MOBILE NO'))
    for contact in db_cursor:
        print('{0:20}{1:5}'.format(contact[0], contact[1]))
    db_cursor.close()


def add_contact():
    contact_name = input("Enter the contact name: ")
    contact_phone = input("Enter the contact phone number: ")
    db_cursor = mydb.cursor()
    query = "INSERT INTO contact (person_name, person_phone) VALUES (%s, %s)"
    values = (contact_name, contact_phone)
    db_cursor.execute(query, values)
    mydb.commit()
    db_cursor.close()
    print("\nContact created!")


def search_contact(contact_name):
    db_cursor = mydb.cursor()
    query = "SELECT * FROM contact WHERE person_name = %s"
    value = (contact_name,)
    db_cursor.execute(query, value)
    contact = db_cursor.fetchone()
    db_cursor.close()
    if contact is None:
        print("Record doesn't exists")
    else:
        print("Contact name: ", contact[0])
        print("Contact number: ", contact[1])


def edit_contact(contact_name):
    db_cursor = mydb.cursor()
    query = "SELECT * FROM contact WHERE person_name = %s"
    value = (contact_name, )
    db_cursor.execute(query, value)
    contact = db_cursor.fetchone()

    if contact is None:
        print("Contact doesn't exists!")
    else:
        while True:
            print("""
        Options to edit
    1. Name
    2. Phone
    3. Back""")
            choice = int(input("Enter: "))
            if choice == 1:
                contact_name_new = input("Enter the new name: ")
                query = "UPDATE contact SET person_name = %s WHERE person_name = %s"
                values = (contact_name_new, contact_name)
                db_cursor.execute(query, values)
                mydb.commit()
                print("Contact updated!")
            elif choice == 2:
                contact_number_new = int(input("Enter the new phone: "))
                query = "UPDATE contact SET person_phone = %s WHERE person_name = %s"
                values = (contact_number_new, contact_name)
                db_cursor.execute(query, values)
                mydb.commit()
                print("Contact updated!")
            elif choice == 3:
                break
            else:
                print("Incorrect option inputed!")


def delete_contact():
    show_contacts()
    print("\nDelete the contact by name or phone number? "
          "\n1. Name "
          "\n2. Phone number")
    option = int(input("Choose the option: "))
    while option not in range(1, 3):
        print("Invalid option!"
              "Options are: 1. Name"
              "             2. Phone number")
    else:
        if option == 1:
            print("What contact do you want to delete by name?")
            name_contact = str(input("Enter name: "))
            db_cursor = mydb.cursor()
            query = "DELETE from contact WHERE person_name = %s"
            value = (name_contact, )
            db_cursor.execute(query, value)
            mydb.commit()
            if db_cursor.rowcount == 0:
                print("Contact not found!")
            else:
                print("Contact deleted!")
        elif option == 2:
            print("What contact do you want to delete by phone number?")
            number_contact = int(input("Enter number: "))
            db_cursor = mydb.cursor()
            query = "DELETE from contact WHERE person_phone = %s"
            value = (number_contact, )
            db_cursor.execute(query, value)
            mydb.commit()
            if db_cursor.rowcount == 0:
                print("Contact not found!")
            else:
                print("Contact deleted!")


if __name__ == '__main__':
    while True:
        x = options()
        if x == 1:
            show_contacts()
        elif x == 2:
            add_contact()
        elif x == 3:
            print("What contact do you want to search?")
            name = input("Name: ")
            search_contact(name)
        elif x == 4:
            name = input("What contact do you want to edit? \nEnter: ")
            edit_contact(name)
        elif x == 5:
            delete_contact()
        elif x == 0:
            exit()
