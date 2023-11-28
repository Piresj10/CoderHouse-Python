#def saludar():
#    print('hola como estas')
#saludar()

# def saludar(nombre):
    # print(f'el se llama {nombre}')
# saludar("carlos vega")

#def retornar_saludar(nombre):
#    mensaje = f'el se llama {nombre}'
#    return mensaje
#print(retornar_saludar("baba"))

#def suma(numero1, numero2):
#    total = numero1 + numero2
#    mensaje = f'El resultado es: {total}'
#    return mensaje
#num1 = int(input("la suma del primer numero es "))
#num2 = int(input("la suma del segundonumero es "))
#print(suma(num1, num2))

#def saludar(city):
#    saludo = f'bienvenido a {city}'
#    return saludo
#print(saludar('Buenos aires'))

# def multiplo(mult,numero):
#     if mult % numero == 0:
#         mensaje = "es multiplo"
#     else:
#         mensaje = "no es multiplo"
#     return mensaje
# number1 = int(input("Valor a comprobar: "))
# number2 = int(input("Si es multiplo de: "))
# print(multiplo(number1, number2))

#def multiplo(numero, n):
#    return [numero * i for i in range(1, n + 1)]
#print(multiplo(7, 10))

# def saludar_ciudad(ciudad):
#     nombre = input("Por favor, introduce tu nombre: ")
#     mensaje = f"¡Hola bienvenido a {ciudad}, {nombre}!"
#     print(mensaje)

# # Ejemplo de uso
# ciudad = input("Introduce el nombre de la ciudad: ")
# saludar_ciudad(ciudad)

# def es_multiplo(numero1, numero2):
#     if numero1 % numero2 == 0 or numero2 % numero1 == 0:
#         return True
#     else:
#         return False

# # Solicitar al usuario dos números enteros
# numero1 = int(input("Ingrese el primer número entero: "))
# numero2 = int(input("Ingrese el segundo número entero: "))

# # Llamar a la función es_multiplo y mostrar el resultado
# if es_multiplo(numero1, numero2):
#     print(f"{numero1} es múltiplo de {numero2} o viceversa.")
# else:
#     print(f"{numero1} no es múltiplo de {numero2} y {numero2} no es múltiplo de {numero1}.")

def anio_bisiesto(anio):
    if not isinstance(anio, int):
        print("Por favor, ingrese un número válido.")
    else:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            print(f"El año {anio} es bisiesto.")
        else:
            print(f"El año {anio} no es bisiesto.")

# Solicitar al usuario un año

anio = int(input("Ingrese un año: "))
anio_bisiesto(anio)






















    
    