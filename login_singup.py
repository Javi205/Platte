# Base de datos ficticia de usuarios (se almacenarán en un diccionario)
basedatos = {}

def registrarse():
    print("Registro de usuario")
    username = input("Ingrese su nombre de usuario: ")
    
    if username in basedatos:
        print("El nombre de usuario ya está en uso.")
        return
    
    password = input("Ingrese su contraseña: ")
    basedatos[username] = password
    print("Registro exitoso.")

def iniciar_sesion():
    print("Inicio de sesión")
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    if username in basedatos and basedatos[username] == password:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

# Menú de la aplicación
while True:
    print("\n1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        registrarse()
    elif opcion == '2':
        iniciar_sesion()
    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

