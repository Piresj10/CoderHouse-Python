#el for siempre se ejecuta en un iterable
#__iter__

#numeros = [1, 2, 3, 4, 5]

#for numero in numeros:
#    print(numero)

#print("gracias por usar nuestro servicio")

#lista = [1,2,3,4,5,6,7,8]
#for num in lista:
#    print("soy un valor de la lista y valgo", num)
#    num *= 5
#    print("Soy un valor de la lista y ahora valgo", num)

#indice = 0
#numeros = [0,1,2,3,4,5,6,7,8]
#for numero in numeros:
#    numeros[indice] *= 5
#    indice += 1
#print(numeros)

#texto = ["Hola mundo, estoy usando for en python "]
#for letra in texto:
#    print(letra)
#texto2 = ""
#for letra in texto:
#    texto2 = letra * 2
#print(texto2)

texto = ["Me gustan los aviones", "Me gusta viajar", "Me gusta la ma;ana", "Me gusta el viento"]
for letra in texto:
    print(f"{letra}, Me gustas tu")
    