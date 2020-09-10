
# # Sumatoria

# suma = 1
# numero = int(input("Ingrese un numero: "))

# while numero >= 0:
#     suma += numero
#     numero = int(input("Ingrese otro un numero: "))

    
#     print(f"La suma de los numeros introducidos es {suma}.")

#Realizar un programa que presente un menú con las siguientes opciones: 

# Imprimimos el menú en pantalla
print("""
    1) Convertir grados a Celsius a Fahrenheit       3) Convertir dólar a pesos
    2) Convertir metros a pies      4) Salir
    """)

# Leemos lo que ingresa el usuario
eligio=input("-Selecciona algo :")

# Según lo que ingresó, código diferente
if eligio=="1":    
    gradoscel = int(input ( "Intruzca la temperatura a convertir: "))
    formula = 9 / 5 * gradoscel + 32
    print (formula)
elif eligio=="2":
    x = 3
    y = 5
    print("x * y = ", x * y)
elif eligio=="3":
    cantidad = float(input ( "Escriba la contidad de efectivo a convertir: "))
    tasa = 60
    operacion = (cantidad * tasa)
    print( operacion)
elif eligio=="4":
    print("Gracias por usar mi programa")
else:
    print("Opción no válida")