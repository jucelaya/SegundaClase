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

# Ejercicios de práctica con cadenas
'''
Enunciado:
Realice un programa que reciba por consola su nombre completo
e imprima en pantalla su nombre en los siguientes formatos:
- Todas las letras en minúsculas
- Todas las letras en mayúsculas
- Solo la primera letra del nombre en mayúscula

NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
de strings:
- lower
- upper
- capitalize

Puede buscar en internet como usar en Python estos métodos.
Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

Link de referencia:
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

¡Cualquier duda con estos métodos pueden consultarnos!

Alumno:
- Crear una una variable llamada nombre_completo
  para almacenar el nombre completo que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Crear una variable llamada nombre_lower
  para almacenar el nombre completo con todas
  las letras transformadas a minúsculas
  por la función lower
  Imprimir en consola el contenido de esta variable

- Crear una variable llamada nombre_upper
  para almacenar el nombre completo con todas
  las letras transformadas a mayúsculas
  por la función upper
  Imprimir en consola el contenido de esta variable

- Crear una variable llamada nombre_capitalize
  para almacenar el nombre completo con
  la primera letra del nombre en mayúscula
  por la función capitalize
  Imprimir en consola el contenido de esta variable

'''

print('Ahora si! buena suerte')
# Empezar aquí la resolución del ejercicio

#Importar la libreria math
import math
#Importar la libreria tkinter (Sirve para crear ventanas ejecutables,
# para que nuestros usuarios puejan ejecutar nuestro código)
import tkinter

#Definimos la variable radio y la obtenemos desde la caja donde se ingresa
# luego realizamos la fórmula para calcular el área del círculo y lo redondeamos
# Finalmente usamos return para mostrar el resultado
def minuscula():
    nombre=str(caja_text1.get())
    nombre2=nombre.lower()
    return var.set(nombre2)
def mayuscula():
    nombre=str(caja_text1.get())
    nombre2=nombre.upper()
    return var.set(nombre2)
def capital():
    nombre=str(caja_text1.get())
    
    
    
    nombre2=nombre.capitalize()
    return var.set(nombre2)

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
text1=tkinter.Label(ventana, text="Ingrese su NOMBRE y APELLIDO")
text1.pack()

#Creamos una caja, donde el usuario ingresará los numeros
#Acomodamos la caja en la ventana
caja_text1=tkinter.Entry(ventana, fg='red')
caja_text1.pack()


#Creamos una botón, para que el usuario presione y ejecute la visualizacion de datos
#Acomodamos el boton en la ventana
boton1=tkinter.Button(ventana,text="Su nombre en minuscula es: ",command=minuscula)
boton1.pack()

boton2=tkinter.Button(ventana,text="Su nombre en mayucula es: ",command=mayuscula)
boton2.pack()

boton3=tkinter.Button(ventana,text="Su nombre capitalizado es: ",command=capital)
boton3.pack()

#Creamos una caja para la salida del resultado y llamamos al resultado
#Acomodamos la caja para mostrar el resultado en la ventana
caja_resultado=tkinter.Label(ventana,textvariable=var)
caja_resultado.pack()

#Finalizamos la ventana
ventana.mainloop()