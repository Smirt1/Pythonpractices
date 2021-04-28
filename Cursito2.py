# print ("hola")
# print("Profe")

# #Variables
# v_texto = "Estamos en"
# year = 2021
# pi = 3.14

# print (v_texto + " el año: " +str (year)) 

# #Entrada de datos

# nacio = input ("En que año nacio?: ")
# edad = ( year - int(nacio))
# print ("En el 2021 cumples " + str(edad) + " años")
 
# #Condiciones
# if edad >= 18 :
#     print("Eres Mayor de edad")
# else:
#     print ("Eres menor de edad")

#  Funciones Area Circulo = Pi * (r*r)   Perimetro = 2*Pi*r

# pi = 3.14
# def circulo ():
#     radio = float(input("cual es el radio (cm)?: "))
#     area = pi * (radio * radio )
#     print ("Area = " + str(area) + "cm")
#     perimetro = 2 * radio * pi
#     print("Perimetro = " + str(perimetro) + "cm")

# circulo()

# v_numero = int(input("numero a elevar?: "))
# def cuadrado(numero):
#     resultado = 0
#     resultado = numero * numero
#     print("Elevado Cuadrado = " + str(resultado))
#     return resultado
    
# cuadrado(v_numero)
# cuadrado(v_numero)

# Listas
# metas = ["Hijo", "Arbol", "Canal_100K", "Viajar", "E_Empresa"]
# print(metas)
# print(metas[3])

# for x in metas:
#     print(x)
    
# print (type(metas))

#While

# z = 1
# while z <= 7:
#     print(z)
#     z = z + 1

#For

# for w in range (20):
#     print(w)


# modo grafico Prueba area del circulo

# from tkinter import *
# arduprofe=Tk()
# arduprofe.title("Ventana de Smirt para Calculo de Circulos")
# pantalla = Entry(arduprofe)
# pantalla.grid(row=1, columnspan=22, sticky=W+E)

# def entra_pantalla (n):
#     pantalla.insert(1, n)
    
# def limpia_pantalla():
#     pantalla.delete(0, END)
    
# def lee_radio():
#     global diametro
#     global radio
#     global area
#     global perimetro
#     lee_pantalla_radio = int (pantalla.get())
#     radio=lee_pantalla_radio
#     diametro = radio+radio
#     area = pi * (radio * radio )
#     perimetro = 2 * pi *radio
#     limpia_pantalla()

# Button(arduprofe,text="DIAMETRO",command=lambda:entra_pantalla("  Diametro="+str(diametro))).grid(row=2, column=0,sticky=W+E)
# Button(arduprofe,text="PERIMETRO",command=lambda:entra_pantalla("  Perimetro="+str(perimetro))).grid(row=2, column=20,sticky=W+E)
# Button(arduprofe,text="AREA",command=lambda:entra_pantalla("  Area="+str(area))).grid(row=3, column=0, sticky=W+E)
# Button(arduprofe,text="BORRAR",command=lambda:limpia_pantalla()).grid(row=3, column=20,sticky=W+E)
# Button(arduprofe,text="LEER RADIO",command=lambda:lee_radio()).grid(row=4, column=0,sticky=W+E)

# arduprofe.mainloop() 

def saludarAlguien(nombre):
	print("Hola lindo" + nombre)

saludarAlguien(" Smirt")
saludarAlguien (" Pedro")
    





