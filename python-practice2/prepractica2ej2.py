#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO

#FIN
lista=[]
for x in range(10):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)
    
for i in lista:
    print(f"Original:{i}")
   
for i in lista:
    if i%2!=0:
        print(f"Impar:{i}")
  
