# Contact book

## <i>Description</i>

This script is designed to keep track of a contact book. With its help you can always find a phone number just by entering the name of the desired person. We can display the contact list any time, add a new contact, search for a contact by the person's phone number / name, edit it or delete it.

## <i>Prerequisites</i>
### Modules used 
|  Name module   |             Description              |
|:--------------:|:------------------------------------:|
| mysqlconnector | `pip install mysql-connector-python` |

## <i>Informations</i>

[MySQL connector module documentation](https://dev.mysql.com/doc/connector-python/en/)

## <u>Running steps</u>
<br>

#### **First of all, you need to create the database *MySQL* for the program:**
  1. Connect to *MySQL*
  2. Run the command `CREATE DATABASE name_for_database;`
  3. Make sure you are running the desired database, use command `USE name_for_database;`
  4. After that, you need to create a table with desired columns `CREATE TABLE name_for_database (person_name VARCHAR(255), person_phone VARCHAR(255));`
#### **You are all set with *MySQL database***
#### **Now we move to *Python***  
- Run the script
- You need to authenticate first to manage the contact book and to make the connection with the *MySQL database*
  1. First time you need to introduce the name of the user used for *MySQL* connection
  2. After this, you need to enter your password for the connection
  3. You need to let *Python* know which database you want to use for this use, you will need to input here the name of your database `name_for_database`
  4. After all of these, the menu will be displayed to let you know all the options available for your contact book
  ```
               1. Show all contacts
  |---------|  2. Add a contact
  | Options |  3. Search a contact
  |---------|  4. Edit a contact
               5. Delete a contact
               0. Close the contact book
  ```
- Now you can manage your own contact book