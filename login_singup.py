print("Crea una cuenta")

username = input("Ingresa tu nombre de usuario: ")
password = input("ingresa tu contraseña: ")

print("Tu cuenta fue creada con exito")
print("Ahora inicia sesión")

username2 = input("Ingresa tu nombre de usuario: ")
password2 = input("ingresa tu contraseña: ")

if username == username2 and password == password2:
    print("Se inició sesión")
else:
    print("usuario o contraseña incorrectas")