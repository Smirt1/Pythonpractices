
# Sumatoria

# suma = 1
# numero = int(input("Ingrese un numero: "))

# while numero >= 0:
#     suma += numero
#     numero = int(input("Ingrese otro un numero: "))
#     if numero == 0:
#         exit(print("Ha salido del sistema"))


#     print(f"La suma de los numeros introducidos es {suma}.")

#Realizar un programa que presente un menú con las siguientes opciones:


# print("""
#     1) Convertir grados a Celsius a Fahrenheit       3) Convertir dólar a pesos
#     2) Convertir metros a pies      4) Salir
#     """)

# opcion=input("-Selecciona algo :")

# if opcion=="1":
#     gradoscel = int(input ( "Introduzca la temperatura a convertir: "))
#     formula = 9 / 5 * gradoscel + 32
#     print (formula)
# elif opcion=="2":
#     metros = float(input ( "Intruzca la cantidad de metros a convertir: "))
#     formula = 3.280840 * metros
#     print(formula)
# elif opcion=="3":
#     cantidad = float(input ( "Escriba la cantidad de efectivo a convertir: "))
#     tasa = 60
#     operacion = (cantidad * tasa)
#     print( operacion)
# elif opcion=="4":
#     print("Gracias por usar mi programa")
# else:
#     print("Opción no válida")

#Hacer un programa que genere las tablas de multiplicar de los números múltiplos de 5 que hay entre 1 y 1000

# def tabla_de_multiplicacion (n):
#     for i in range (1, 1000):
#         print (n,'*',i, '=',i * n)


# tabla_de_multiplicacion (5)

#Aplicacion para calcular ISR (ver tabla DGII), ARS, y AFP


top1 = 416220.00
top2 = 624329.00
top3 = 867123.00
salario = float(input("Ingresa tu sueldo mensual:"))
salario_anual = salario * 12
imp = 0


if salario_anual <= top1:
    print("Cuenta Excenta")

elif salario_anual >= top3:
    imp = salario * 0.0125
    afp = salario * (0.071 / 12)
    ars = salario * (0.0709 / 12)
    too = afp + imp + ars
    print(f"Impuesto mensual de AFP {afp}")
    print(f"Monto mensual de ars es:{ars}")
    res = salario - too
    afp = salario * 0.071
    print(f"Total de impuestos es de:{imp}")
    print(f"Monto mensual de impuestos:{too}")
    total = res * 12
    print(f"El monto con isr es de:{too*12}")
    total2 = salario_anual - (imp * 12) - (afp * 12) - (ars * 12)
    print(f"Monto anual con todos los impuestos {total2}")

else:
    imp = salario * 0.01666
    afp = salario * (0.071/12)
    ars = salario * (0.0709/12)
    too = afp + imp + ars
    print(f"Impuesto mensual de AFP {afp}")
    print(f"Monto mensual de ars:{ars}")
    res = salario - too
    afp = salario * 0.071
    print(f"Total mensual de isr es de:{imp}")
    print(f"Monto mensual de impuestos:{too}")
    total = res * 12
    print(f"El monto con anual es de:{too*12}")
    total2 = salario_anual - (imp*12) - (afp*12) - (ars*12)
    print(f"Monto anual con todos los impuestos {total2}")


#  Cajero

