# Calculadora de ISR

tope1 = 416220.00
tope2 = 642329.00
tope3 = 867123.00
salario = float (input ("Ingrese su sueldo mensual por favor: "))
salario_anual = salario * 12
isr = 0;

if salario_anual <= tope1:
    print ("Excento")
elif salario_anual <= tope2:
    excedente = salario_anual - tope1
    isr = excedente * 0.15
elif salario_anual <= tope3:
    excedente = salario_anual - tope2
    isr =31216.00 + (excedente * 0.20)
else:
    excedente = salario_anual - tope3
    isr = 79776.00 + excedente * 0.25

print (isr / 12)
