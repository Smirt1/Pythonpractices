
# # Sumatoria

# suma = 1
# numero = int(input("Ingrese un numero: "))

# while numero >= 0:
#     suma += numero
#     numero = int(input("Ingrese otro un numero: "))

    
#     print(f"La suma de los numeros introducidos es {suma}.")

#Realizar un programa que presente un menú con las siguientes opciones: 


print("""
    1) Convertir grados a Celsius a Fahrenheit       3) Convertir dólar a pesos
    2) Convertir metros a pies      4) Salir
    """)

opcion=input("-Selecciona algo :")

if opcion=="1":    
    gradoscel = int(input ( "Introduzca la temperatura a convertir: "))
    formula = 9 / 5 * gradoscel + 32
    print (formula)
elif opcion=="2":
    metros = float(input ( "Intruzca la cantidad de metros a convertir: "))
    formula = 3.280840 * metros
    print(formula)
elif opcion=="3":
    cantidad = float(input ( "Escriba la cantidad de efectivo a convertir: "))
    tasa = 60
    operacion = (cantidad * tasa)
    print( operacion)
elif opcion=="4":
    print("Gracias por usar mi programa")
else:
    print("Opción no válida")