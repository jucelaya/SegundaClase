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

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
El objetivo es realizar un programa que consulte por consola:
- El nombre completo de una persona
- El número de identificación de una persona
- La edad de una persona
- La altura de una persona

Finalmente el programa debe imprimir los contenidos
de las variables generadas durante el programa en el siguiente
formato, dos líneas de texto por separado (dos print separados):
- Un print debe imprimir el nombre completo y el DNI.
        Ej: Juan Carlos 35205070
- El segundo print debe imprimir la edad y la altura.
        Ej: 38 1.70

Alumno:
- Crear una una variable llamada nombre_completo
  para almacenar el nombre completo que usted
  debe ingresar por consola con la función input.
  Recuerde en este caso utilizar el input junto a str.

- Crear una una variable llamada identificacion
  para almacenar el número de identificación que usted
  debe ingresar por consola con la función input.
  Recuerde en este caso utilizar el input junto a int.
  IMPORTANTE: Solo ingresar números, sin puntos o guiones

- Crear una una variable llamada edad
  para almacenar la edad que usted
  debe ingresar por consola con la función input.
  Recuerde en este caso utilizar el input junto a int.

- Crear una una variable llamada altura
  para almacenar la altura que usted
  debe ingresar por consola con la función input.
  Recuerde en este caso utilizar el input junto a float.

'''

print('Sistema de ingreso de datos')
# Empezar aquí la resolución del ejercicio
#Importar la libreria math
import math
#Importar la libreria tkinter (Sirve para crear ventanas ejecutables,
# para que nuestros usuarios puejan ejecutar nuestro código)
import tkinter

#Definimos la variable radio y la obtenemos desde la caja donde se ingresa
# luego realizamos la fórmula para calcular el área del círculo y lo redondeamos
# Finalmente usamos return para mostrar el resultado
def full_name():
    nombre=str(caja_text1.get())
    apellido=str(caja_text2.get())
    full_name=nombre+' '+apellido
    return var.set(full_name)
def edad():
    edad=int(caja_text3.get())
    return var.set(edad)
def peso():
    peso=float(caja_text4.get())
    return var.set(peso)

#Creamos la ventana
ventana=tkinter.Tk()

#Colocamos su titúlo a nuestra ventana
ventana.title ("@JUCELAYA")

#Definimos el tamañaño de nuestra ventana
ventana.geometry("400x400+450+200")

#Creamos la variable que nos ayudará amostrar en pantalla y la definimos como
# un Double (Número con decimales)
var=tkinter.DoubleVar()

#creamos la descripción de nuestra venta
text2=tkinter.Label(ventana, text="Esta ventana permite ingresar sus datos", bg='blue', fg='white')
text2.pack()

#Creamos el texto que se imprime en pantalla
#para solicitar los numeros
#Acomodamos el texto en la ventana
text1=tkinter.Label(ventana, text="Ingrese su nombre y apellido")
text1.pack()

#Creamos una caja, donde el usuario ingresará los numeros
#Acomodamos la caja en la ventana
caja_text1=tkinter.Entry(ventana, fg='red')
caja_text1.pack()
caja_text2=tkinter.Entry(ventana, fg='red')
caja_text2.pack()

text3=tkinter.Label(ventana, text="Ingrese su edad")
text3.pack()

caja_text3=tkinter.Entry(ventana, fg='blue')
caja_text3.pack()

text4=tkinter.Label(ventana, text="Ingrese su peso")
text4.pack()

caja_text4=tkinter.Entry(ventana, fg='blue')
caja_text4.pack()
#Creamos una botón, para que el usuario presione y ejecute la visualizacion de datos
#Acomodamos el boton en la ventana
boton1=tkinter.Button(ventana,text="Su nombre es: ",command=full_name)
boton1.pack()

boton2=tkinter.Button(ventana,text="Su edad es: ",command=edad)
boton2.pack()

boton3=tkinter.Button(ventana,text="Su peso es: ",command=peso)
boton3.pack()

#Creamos una caja para la salida del resultado y llamamos al resultado
#Acomodamos la caja para mostrar el resultado en la ventana
caja_resultado=tkinter.Label(ventana,textvariable=var)
caja_resultado.pack()

#Finalizamos la ventana
ventana.mainloop()
