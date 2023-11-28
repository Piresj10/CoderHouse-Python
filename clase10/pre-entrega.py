import json
# Crear un diccionario para almacenar los usuarios y contraseñas
usuarios = {}

# Función para registrar un nuevo usuario
def registrar_usuario():
    usuario = input("Ingrese un nombre de usuario: ")
    contraseña = input("Ingrese una contraseña: ")
    usuarios[usuario] = contraseña
    print("Usuario registrado exitosamente.")


# Función para mostrar la información de usuarios
def mostrar_usuarios():
    print("Lista de usuarios registrados:")
    for usuario, contraseña in usuarios.items():
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

# Función para realizar el login
def login():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.") 
      
# Momento de loguear
while True:
    print("\nSeleccione una opción:")
    print("1. Registrar un nuevo usuario")
    print("2. Mostrar la información de usuarios")
    print("3. Iniciar sesión")

    
    opcion = input("Opción: ")
    
    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        mostrar_usuarios()
    elif opcion == "3":
        login()
    else:
        print("Opcion incorrecta. Por favor, elija una opcion correcta")
    
    # Aca estamos guardando los datos en un archivo .txt con json
    user_txt = json.dumps(usuarios, indent=2) 
    with open("user.txt", "w") as fil:
        fil.write(user_txt)
   
