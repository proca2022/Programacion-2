#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
try:
    num1 = int(input('Ingrese un primer numero entero: '))
    num2 = int(input('Ingrese un segundo numero entero: '))
    print(num1 / num2)
except ZeroDivisionError:
    print("No se puede dividir por cero")
