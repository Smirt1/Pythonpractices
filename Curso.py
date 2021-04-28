

#print("Hola! Dime tu nombre")
#nombre = input()
#print ("Hola, bienvenido")
#print (nombre)

#print ("Dime un numero")
#primerNumero = int(input())
#print ("Dime otro numero")
#segundoNumero = int(input())
#print ("Su suma es")
#print (primerNumero * segundoNumero)


#print("Vino la lluvia\ny se la llevó.")

#print("Mi nombre es", "Python.", end=" ")
#print("Monty Python.")

#print("Me gusta \"Monty Python\"")

#print ("Me gusta \"Smirt Valentin\"")

#print (4 ** 2)

#print (2 + 3 * 5)


#print(2 * 3 % 5)

#var = 1
#print(var)

#var = 1
#balance_cuenta = 10000.0
#nombre_cliente = 'Smirt'
#print (var,balance_cuenta,nombre_cliente)
#print (var)

#var = "3.0"
#print ("Mi version de Linux es: " + var)

juan = 3
maria = 5
tulio = 6

print (juan, maria, tulio)
totalmanzanas = (juan + maria + tulio)
print (" El total de manzanas es: ", totalmanzanas)


# kilometros = 12.25
# millas = 7.38

# millas_a_kilometros = (millas * 1.6)
# kilometros_a_millas = (kilometros * 0.62)

# print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
# print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")

# print ("Dime tu edad")
# edad = input()
# print ("Tu edad es", edad)

# print ("Cual es tu peso?")
# peso = input ()

# nom = input("¿Me puedes dar tu nombre por favor? ")
# ape = input("¿Me puedes dar tu apellido por favor? ")
# print("Gracias.")
# print("\nTu nombre es " + nom + " " + ape + ".")

# ingresa un valor flotante para la variable a aquí
# ingresa un valor flotante para la variable b aquí

# valor_a = float(input("Ingresa valor a: "))
# valor_b = float(input("Ingresa valor b: "))

# # muestra el resultado de la suma aquí 

# suma = (valor_a + valor_b)
# print ("El resultado de la suma es: ", suma)

# # muestra el resultado de la resta aquí

# resta = (valor_a - valor_b)
# print ("El resultado de la resta es: ", resta)

# # muestra el resultado de la Multipicacion aquí

# mult = (valor_a * valor_b)
# print ("El resultado de la multiplicacion es: ", mult)

# # muestra el resultado de la división aquí

# divi = (valor_a / valor_b)
# print ("El resultado de la division es: ", divi)

# print ("Eres el mejor")


hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
 
# calcula los minutos y los convierte a una cadena
minutos=str((min+dura) %60)
# calcula los minutos totales y luego lo convierte a horas y despues a una cadena
horas= str( ((hora*60 + min + dura)//60) % 24)
 
 
print("Hora: " +horas +":" +minutos)



#Silvestre