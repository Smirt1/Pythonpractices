#Practiva 1: Variables, tipos de datos, expresiones y condicionales.

#Escriba en pantalla el tipo de dato que retorna la expresión 4 < 2

# comparacion = 4 < 2
# print (comparacion)

#Almacene en una variable el nombre de una persona y al final muestre en la consola el me nsaje:

# nombre = "Pedro Suarez"
# print ("Bienvenido: " + nombre)

#Evalúe si un número es par o impar y muestre en la consola el mensaje.

# numero = 15
# if numero % 2 == 0:
#  print("Par")
# else:
#     print("Es Impar")

#Almacene dos números y evalúe si el primero es mayor que el segundo. El resultado debe verse en la consola.

# numero1 = 5
# numero2 = 10
# resultado = numero1 >= numero2
# print(resultado)

#Convierta dólares a pesos.

# cantidad = float(input ( "Escriba la contidad de efectivo a convertir: "))
# tasa = 60
# operacion = (cantidad * tasa)
# print( operacion)

#Convierta grados celsius a Fahrenheit

# gradoscel = int(input ( "Intruzca la temperatura a convertir: "))
# formula = 9 / 5 * gradoscel + 32
# print (formula)

# Almacene cuatro notas 90,95,77, 92 y las promedie. Al final debe decir su calificación en letras A, B,C,D, E ó F.

# nota1 = 90
# nota2 = 95
# nota3 = 77
# nota4 = 92

# sumatoria = nota1 + nota2 + nota3 + nota4
# promedio = sumatoria / 4
# print (promedio)
# if promedio >= 90:
#     print("Su nota es A")
# elif promedio <= 89:
#     print ("Su nota es B")
# elif promedio <= 79:
#     print("Su nota es C")
# elif promedio <= 69:
#     print("Su nota es D")
# elif promedio <= 59:
#     print("Su nota es E")
# elif promedio <= 49:
#     print("Su nota es F")

#Que almacene monto, cantidad de cuotas, y porcentaje de interés anual de un préstamo y calcule la cuota mensual. (Amortizar mediante el sistema francés)

R = 0
prestamo = float (input ("Ingrese el valor del prestamo: "))
interes = float (input ("Ingrese la tasa solicitada:"))
cuotas = int(input ("Ingrese el tiempo a pagar:"))
R = prestamo * ((interes * (1 + interes) * cuotas) / ((1 + interes) * cuotas -1))
print (R)













