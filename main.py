from database import *


def print_menu():
    print("""
    1-Log in
    2-Sign up
    3-Exit""")

def login_menu(user):
    print("""
    {user[1]} {user[2]} {user[3]}
    
    1-Video link
    2-Article link
    3-Soundcloud link
    4-Exit
    """)

while True:
    print_menu()
    choice1=input("> ")

    if  choice1 == "1":
        username = input("Username : ")
        password = input("Password : ")
        search = search_username(username)
        if search is None:
            print("No such user exists. ")
            continue
        elif password==search[4]:
            login_menu(search)
            choice2=input(">")
            if choice2 =="1":
                #video
            elif choice2=="2":
                #text
            elif choice2=="3":
                #soundcloud
            elif choice2=="4":
                break
            continue
    
    elif choice1=="2":
        username=input("Username : ")
        password= input ("Password : ")
        search=search_username(username)
        if search is not None:
            print("This username already exists. ")
            continue
        insert(username,password)
        print("Successfully signed up!")
    elif choice1 == "3":
        break