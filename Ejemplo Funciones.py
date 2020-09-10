# Funciones en python

def saludar():

	print("Hola a todos!")

# invocar
saludar()
saludar()


# parametros

def saludarAlguien(nombre):
	print("Hola "  + nombre)

saludarAlguien("Smirt")
saludarAlguien ("Pedro")
saludarAlguien ("Lucas")

def duplicar (x):
    res = x * 2
    return res

duplicado = duplicar (130)
print (duplicado)