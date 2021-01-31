from DatabaseHandle import CreateDatabase,ShowValues,DeleteRecords,InsertEntry
from PasswordRecomendation import PasswordGenerator
import hashlib
import getpass
import os

path=os.getcwd()
if not os.path.exists(f"{path}\\my-test.db"):
    try:
        CreateDatabase()
    except OSError:
            print (f"database creation failed")
else:
    pass


def menu():
    print('#'*30)
    print(('#'*12) +(' ') + 'Menu'+(' ')+ ('#' *12))
    print('1. Insert new entry | EX:email,password,username,url,app_name')
    print('2. Show all emails and passwords')
    print('3. Delete all previous records')
    print('4. Password Recomendation')
    print('Q. Exit')
    print('#'*30)
    print("\n\n\n")

user_input=getpass.getpass() 
Password='admin'
if hashlib.sha256(user_input.encode()).hexdigest() == hashlib.sha256(Password.encode()).hexdigest():
    while True:
        menu()

        option=str(input("Enter option: "))
        if option == str(1):
            email,password,username,url,app_name = input().split(',') 
            InsertEntry(email,password,username,url,app_name)
        
        elif option == str(2):
            ShowValues()
        
        elif option == str(3):
            DeleteRecords()

        elif option == str(4):
            print("recomended password : "+ PasswordGenerator())
            input("press enter to continue!!!!")
            print('\n\n')
        
        elif option.upper() == 'Q'.upper():
            break
        else:
            print("enter a valid input!!")
else:
    print('#'*30)
    print("Master Password is wrong exiting!!!")
    print('#'*30)