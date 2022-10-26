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
El objetivo es realizar un programa que determine
cual sería el apellido de una persona
al ingresara los dos nombres completos de sus padres/madres/tutores.
(un solo nombre y un solo apellido en cada caso)
En definitiva se solicita crear una variable nueva que reuna
los dos apellidos.

- Consultar e ingresar por consola el primer nombre completo
- Consultar e ingresar por consola el segundo nombre completo
- Luego debe consultar solo nombre del hijo/a
- Debe extraer los apellidos de los padres (ver la nota al final)
- Luego formar el nombre completo del hijo/a utilizando los apellidos
  de sus padres/madres/tutores y el nombre del hijo/a
- Imprimir en pantalla el resultado

NOTA: Para extraer el apellido del nombre completo recomendamos usar
el método "split"
Mostraremos un ejemplo:

direccion_completa = 'Monroe 2716'
calle, altura = direccion_completa.split(' ')

Les dejamos por su cuenta a que busquen un poco más
acerca de este método llamado split, que seguramente
utilizarán mucho de acá en adelante.
Les dejamos un link con algunos ejemplos más:
https://www.pythonforbeginners.com/dictionary/python-split

¡Cualquier duda con el método split pueden consultarnos!

Alumno:
- Crear una una variable llamada nombre_completo_1
  para almacenar el primer nombre completo que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Crear una una variable llamada nombre_completo_2
  para almacenar el primer nombre completo que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Crear una una variable llamada nombre
  para almacenar el nombre del hijo/a que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Cuando utilice la función split para dividir
  el nombre_completo_1, almacene los resultados
  en las variables llamadas nombre_1 y apellido_1
  Imprimir en consola el contenido de estas variables

- Cuando utilice la función split para dividir
  el nombre_completo_2, almacene los resultados
  en las variables llamadas nombre_2 y apellido_2
  Imprimir en consola el contenido de estas variables

- Crear una una variable llamada hijo
  para almacenar el nombre del hijo/a contenido en
  la variable nombre sumando/concatenando
  los apellidos almaecnados en apellido_1 y apellido_2
  Imprimir en consola el contenido de esta variable

'''

print('Jugando con texto')
# Empezar aquí la resolución del ejercicio
#Importar la libreria math
import math
#Importar la libreria tkinter (Sirve para crear ventanas ejecutables,
# para que nuestros usuarios puejan ejecutar nuestro código)
import tkinter

#Definimos la variable radio y la obtenemos desde la caja donde se ingresa
# luego realizamos la fórmula para calcular el área del círculo y lo redondeamos
# Finalmente usamos return para mostrar el resultado
def hijo():
    nombre_apellido_1=str(caja_text1.get())
    nombre_apellido_2=str(caja_text2.get())
    nombre_hijo=str(caja_text3.get())
    nombre1, apellido1 = nombre_apellido_1.split()
    nombre2, apellido2 = nombre_apellido_2.split()
    hijo_r = nombre_hijo+' '+ apellido1 + ' '+ apellido2
    hijo1 = hijo_r.upper()
    return var.set(hijo1)

    
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
text1=tkinter.Label(ventana, text="Ingrese su NOMBRE y APELLIDO del PADRE")
text1.pack()

#Creamos una caja, donde el usuario ingresará los numeros
#Acomodamos la caja en la ventana
caja_text1=tkinter.Entry(ventana, fg='red')
caja_text1.pack()

text2=tkinter.Label(ventana, text="Ingrese su NOMBRE y APELLIDO de la MADRE")
text2.pack()

#Creamos una caja, donde el usuario ingresará los numeros
#Acomodamos la caja en la ventana
caja_text2=tkinter.Entry(ventana, fg='red')
caja_text2.pack()
#Creamos una botón, para que el usuario presione y ejecute la visualizacion de datos
#Acomodamos el boton en la ventana

text3=tkinter.Label(ventana, text="Ingrese su nombre de su HIJO")
text3.pack()

#Creamos una caja, donde el usuario ingresará los numeros
#Acomodamos la caja en la ventana
caja_text3=tkinter.Entry(ventana, fg='red')
caja_text3.pack()

boton1=tkinter.Button(ventana,text="El nombre de su hijo es: ",command=hijo)
boton1.pack()

#Creamos una caja para la salida del resultado y llamamos al resultado
#Acomodamos la caja para mostrar el resultado en la ventana
caja_resultado=tkinter.Label(ventana,textvariable=var)
caja_resultado.pack()

#Finalizamos la ventana
ventana.mainloop()
