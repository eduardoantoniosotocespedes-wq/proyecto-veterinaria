from usuario import costumer
from administrador import administrator




users =[]
user_passwords=[]
admins=["admin1"]
admins_passwords =["contraseña"] 
adimins_id =[12345]

def verify():
    while True:
        print("================= MENU DE LOGIN ==================")
        user = str(input("Porfavor ingrese su usuario: ")).strip().lower()
        password =str(input("Porfavor ingrese su contraseña: ")).strip()
        if user in users:
            user_1 = users.index(user) #buscando la pocicion en la lista
            if user_passwords[user_1] == password:
                user_admin()
            else:
                print("==== Usuario o contraseña incorrecta ====")
        elif user in admins:
            user_1 = admins.index(user) #buscando la pocicion en la lista
            if admins_passwords[user_1] == password:
                user_admin()
                break
            else:
                print("""
= Usuario o contraseña incorrecta intenta denuevo =
""")
        else:
            print("""
=========== ERROR =====================================
== Usuario no registrador                           ===
== Comuniquese con el administrador para registrarse ==
== Administrador: 64946952                          ===
== Para intentar denuevo ingrese 1                  ===
== Para finalizar login ingrese cualquier tecla     ===
""")
            option = input("== Responde aqui: ")
            if option == "1" or option == 1:
                print("""
======= Volviendo...                         ==========
""")
            else:
                print(""""
======= Saliendo...                          ==========
 """)
                break
def user_admin():
    while True:
        print("""
================= MENU PRINCIPAL =================
Desea entrar como:
1.-Usuario
2.-Administrador """)
        option =(input("responda aqui: ")).upper().strip()#identificar si pone un numero o letra
        if option.isdigit():
            option = int(option)
            match option:
                case 1:
                    costumer()
                    break
                case 2:
                    print("""
======= VERIFICACION PARA ADMINISTRADORES ========""")
                    user = input("Ingrese su usuario: ")
                    clave = int(input("Ingrese su numero de ID: "))
                    if user in admins:
                        user_1 = admins.index(user)#buscando la pocicion en la lista
                        if adimins_id[user_1] == clave:
                            administrator()
                        else:
                            print("===ERROR===")  
                    else:
                        print("""
=== No hay ningun administrador con ese nombre       ====
=== LLAMANDO A LA POLICIA.....                       ====
=== bromita, para intentar denuevo precione: 1       ====
=== para terminar el login precione cualquier tecla  ====""")             
                        option = input("== Responde aqui: ")
                        if option == "1" or option == 1:
                            print("""
======= Volviendo...                         ==========
""")
                        else:
                            print(""""
======= Saliendo...                          ==========
 """)
                            break
                case _:
                    print("Opcion equivocada, intente denuevo.")
        else:
            option = str(option)    
            print("===Opcion invalida, intente denuevo.")

def register_user():
    pass
def show_user():
    pass
def search_user():
    pass
def modify_user():
    pass
def delete_user():
    pass