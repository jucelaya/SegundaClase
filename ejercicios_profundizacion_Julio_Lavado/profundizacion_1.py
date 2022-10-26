# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
- El objetivo será realizar un calculadora,
- Se ingresará por consola dos números decimales (float)
- Se deberá calcular todas las operaciones entre ellos:
A) Suma  --> primero número más el segundo    
B) Resta --> primero número menos el segundo
C) Multiplicación --> primero número por el segundo
D) División --> primero número dividido el segundo
E) Exponente/Potencia --> primero número exponente el segundo

- Para todos los casos se debe imprimir en pantalla
  el resultado de la operación realizada

Alumno:
- Crear una una variable llamada numero_1
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada numero_2
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Almacenar el valor de cada operación realizada en las
  variables que usted creará con los siguientes nombres:
  suma, resta, multiplicacion, division, potencia

- Al final imprimir todos los resultados almacenados
  en esas variables
'''

#print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

import math
#Importar la libreria tkinter (Sirve para crear ventanas ejecutables,
# para que nuestros usuarios puejan ejecutar nuestro código)
import tkinter

#Definimos la variable radio y la obtenemos desde la caja donde se ingresa
# luego realizamos la fórmula para calcular el área del círculo y lo redondeamos
# Finalmente usamos return para mostrar el resultado
def suma():
    numero_1=float(caja_text1.get())
    numero_2=float(caja_text2.get())
    suma=numero_1+numero_2
    return var.set(suma)

def resta():
    numero_1=float(caja_text1.get())
    numero_2=float(caja_text2.get())
    resta=numero_1-numero_2
    return var.set(resta)

def multiplicacion():
    numero_1=float(caja_text1.get())
    numero_2=float(caja_text2.get())
    multiplicacion=numero_1*numero_2
    return var.set(multiplicacion)

def division():
    numero_1=float(caja_text1.get())
    numero_2=float(caja_text2.get())
    division=numero_1/numero_2
    return var.set(division)
#Creamos la ventana
ventana=tkinter.Tk()

#Colocamos su titúlo a nuestra ventana
ventana.title ("@JUCELAYA")

#Definimos el tamañaño de nuestra ventana
ventana.geometry("400x200+450+200")

#Creamos la variable que nos ayudará amostrar en pantalla y la definimos como
# un Double (Número con decimales)
var=tkinter.DoubleVar()

#creamos la descripción de nuestra venta
text2=tkinter.Label(ventana, text="Esta ventana permite sumar numeros", bg='blue', fg='white')
text2.pack()

#Creamos el texto que se imprime en pantalla
#para solicitar los numeros
#Acomodamos el texto en la ventana
text1=tkinter.Label(ventana, text="Ingrese los números")
text1.pack()

#Creamos una caja, donde el usuario ingresará los numeros
#Acomodamos la caja en la ventana
caja_text1=tkinter.Entry(ventana, fg='red')
caja_text1.pack()
caja_text2=tkinter.Entry(ventana, fg='blue')
caja_text2.pack()
#Creamos una botón, para que el usuario presione y ejecute la operación
#Acomodamos el boton en la ventana
boton1=tkinter.Button(ventana,text="+",command=suma)
boton1.pack()

boton2=tkinter.Button(ventana,text="-",command=resta)
boton2.pack()

boton3=tkinter.Button(ventana,text="x",command=multiplicacion)
boton3.pack()

boton4=tkinter.Button(ventana,text="/",command=division)
boton4.pack()

#Creamos una caja para la salida del resultado y llamamos al resultado
#Acomodamos la caja para mostrar el resultado en la ventana
caja_resultado=tkinter.Label(ventana,textvariable=var)
caja_resultado.pack()

#Finalizamos la ventana
ventana.mainloop()