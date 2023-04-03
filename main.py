from veritabani import *


def print_menu():
    print("""
    1-Giris Yap
    2-Kayıt ol
    3-Kapat""")

def login_menu(user):
    print("""
    {user[1]} {user[2]} {user[3]}
    
    1-kullanici arama
    2-tüm kullanicilari yazdir
    3-hesabımı sil
    4-çıkış yap
    """)



while True:
    print_menu()
    secim=input("Secim :")
    if secim == "1":
        username = input("Kullanici adi : ")
        password = input("Sifre : ")
        search = search_username(username)
        if search==None:
            print("Boyle bir kullanici yok")
            continue
        if password==search[4]:
            while True:
                login_menu(search)
                secim=input("secim:")
                if secim =="1":
                    u=input("kullanici adi ")
                    birisi =search_username(u)
                    if birisi == None:
                        print("kullanici bulunamadi")
                        continue
                    print(f"{birisi[1]}{birisi[2]}{birisi[3]}")
                    if secim=="2":
                        print_all
                    if secim=="3":
                        delete_account(username)
                        break
                    if secim=="4":
                        break
                    continue
    
    if secim=="2":
        name=input("adiniz : ")
        lastname = input("soyadiniz : ")
        password= input ("sifreniz : ")
        search=search_username(username)
        if search != None:
            print("Bu kullanici adi zaten var")
            continue
        insert(name, lastname, username,password)
        print("kayit basarili")
    if secim == "3":
        break