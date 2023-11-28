#1. abrir el archivo (obligatorio)
# A. ruta donde se encuentra el archivo 
# B. que permisos voy a brindar al archivo, a -> adicion al archivo, w -> sobreescritura -> rb lectura binaria

#2. escribir el archivo
#3. cerrar el archivo (obligatorio)

#escritura
# fil = open("usuario.csv", "a")
# fil.write("\njavier2, alejandro2, pires2, 292")
# fil.close()

# with open("miHobbieFavori.txt", "w") as archivo:
#     for i in range(3):
#         hobby = input(f"Ingrese su hobby favorito {i+1}: ")
#         archivo.write(f"Hobby {i+1}: {hobby}\n")

# print("Hobbies favoritos guardados en el archivo 'miHobbieFavorito.txt'.") 

#lectura
# read lectura completa
# readline lectura de una sola linea
# readlines iterable con la lectura de todas las lineas

#with open("usuario.csv") as archivo:
    # print(archivo.read())
    # print(archivo.readline())
    #print(archivo.readlines())
    
 
# import json   
# user_dic = {
#     "estudiantes": [
#         {
#             "nombre": "Luis",
#             "edad": 34
#         },
#         {
#            "nombre": "marcos",
#             "edad": 35
#         },
#         {
#             "nombre": "tito",
#             "edad": 23
#         },
#     ]
# }
# user_str = json.dumps(user_dic, indent=2) #de dict a str
# with open("estudiantes.txt", "w") as fil:
#     fil.write(user_str)

# import json
# with open("estudiantes.txt", "r") as fil:
#     estudiantes_str = fil.read()

# estudiantes_dict = json.loads(estudiantes_str) #de str a dict
# print(estudiantes_dict["estudiantes"][1]["nombre"])


# with open("resultados-del-test.csv", "r") as fil:
#     i = 0
#     for line in fil.readlines():
#         print(line)        
#         i += 1
#         if i == 10:
#             break

# import pandas
# datos = pandas.read_csv("resultados-del-test.csv")
# print(datos.edad.head(5))
# pass

with open("hola.txt", "w") as archivo:
    archivo.write("hola")
  
        



