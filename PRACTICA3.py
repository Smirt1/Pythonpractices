#Hacer una función que potencie un número x a la y

# valor = 20
# potencia = 2

# def pontenciar(a, b):
#     x = a ** b
#     return print(x)

# pontenciar(valor, potencia)

#Realizar una función que pida por pantalla un número del 1 al 10 y muestre por pantalla el número escrito en letras.

# def numeros_a_letras():
#     n = int(input("Dame un número del 1 al 10: "))

#     if n > 10:
#         print("Valiste vergas, te pedí un numero del 1 al 10")
#     elif n == 1:
#         print("Uno")
#     elif n == 2:
#         print("Dos")
#     elif n == 3:
#         print("Tres")
#     elif n == 4:
#         print("Cuatro")
#     elif n == 5:
#         print("Cinco")
#     elif n == 6:
#         print("Seis")
#     elif n == 7:
#         print("Siete")
#     elif n == 8:
#         print("Ocho")
#     elif n == 9:
#         print("Nueve")
#     elif n == 10:
#         print("Diez")

# numeros_a_letras()

#Hacer una función que reciba un año como argumento y retorne verdadero si es bisiesto.

# def año_bisiesto(a):

#     if a % 4 == 0:
#         if a % 100 == 0:
#             if a % 400 == 0:
#                 print(True)
#             else:
#                 print(False)
#         else:
#             print(True)
#     else:
#         print(False)


# año_bisiesto(1900)
# año_bisiesto(2012)
# año_bisiesto(2020)
# año_bisiesto(2021)
# año_bisiesto(2022)
# año_bisiesto(2023)
# año_bisiesto(2024)

#Crear una función que evalúe dos números y retorne verdadero si ambos números son iguales.

# def igualdad(x, y):
#     if x == y:
#         print(True)
#     else:
#         print(False)

# # Se pone en ejecución la función
# igualdad(1, 5)
# igualdad(2, 2)


# igualdad(10/2, 5)
# igualdad(pow(10, 2), 100)


# Un número palindrómico se lee igual en ambos sentidos.El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.
# Cree una función que encuentre el palíndromo más grande hecho del producto de dos números de 3 dígitos.

# def esPalindromo(num):
#     return str(num) == str(num)[::-1]

# def masGrande(num1, num2):
#     z = 0
#     for x in range(num2, num1, -1):
#         for y in range(num2, num1, -1):
#             if esPalindromo( x * y):
#                 if x * y > z:
#                     z = x * y
#     return z


# print(masGrande(100,999))

# print(masGrande(191,121))

 #Hacer una función que reciba una cedula como argumento y diga si la cedula es válida o no.

# def comprador_cedulas():
#     cedula = input("Introduzca la cedula a comprobar sin guiones: ")
#     # Se hace uso de la función len() para comprobar si la longitud de los caracteres es mayor que 11
#     if len(cedula) > 11:
#         print("Cédula incorrecta")
#     else:
#         print("Cédula válida")

# comprador_cedulas()

# Hacer una función que reciba como argumento una lista de elementos numéricos y retorno otra lista con cada elemento de la primera lista duplicados.

# def duplicador(lista):

#     lista = lista
#     # Con el ciclo for se recorre todos los datos de la lista
#     for i in range(len(lista)):
#     # Se imprime los valores de la lista con el índice i y se duplica
#         print(lista[i] * 2)

# duplicador([2, 4, 6, 8, 10])


# 8- Hacer una función que reciba un valor iniciar y uno final, y muestre en pantalla las tablas de multiplicar de los números múltiplos de 6 que hay
# entre el valor inicial y el valor final.

def tabla_multiplicar_num4(v_inicial, v_final):
    n = 4 

    if v_inicial > v_final:
        print("Error: Valor Inicial debe ser menor al Valor Final")
    else:
        while v_inicial <= v_final:
            res =  n * v_inicial
            print(f"{n} X {v_inicial} = {res}")
            v_inicial += 1


tabla_multiplicar_num4(1, 10)

tabla_multiplicar_num4(11, 20)

tabla_multiplicar_num4(10, 1)