#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO


#FIN

lista=[]
#disponemos un ciclo de 2 vueltas
for x in range(2):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)

#imprimimos la lista    
print(lista)
print('Máximo', max(lista))