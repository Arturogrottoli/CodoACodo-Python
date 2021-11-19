#ejercicio 5

import sys
print('Ejercicio 5')

cl= int (input ('Ingrese la cantidad de lapices:'))

if cl >= 1000:
    print('Precio final =  ', cl*0.85)

else:
    print('Precio final =  ', cl*0.9)


#Ejercicio 6

sys.stdin.readline
print('Ejercicio 6')

personas= int (input ('Ingrese la cantidad de personas:'))

if personas < 200:
    print('Precio final =$  ', personas*95)
elif (personas >= 200 and personas<=300):
    print('Precio final =$  ', personas*85)

else:
    print('Precio final =$  ', personas*75)


#Ejercicios While

import sys
print('Ejercicio 1')
contador = 1
while contador < 11:
    print(contador)
    contador = contador+1

#Ejercicios For

import sys
print('Ejercicio 1')
#imprimir los num de 0 al 20

for x in range(21):
    print(x)


sys.stdin.readline()
print('Ejercicio 2')
#del 10 al 20

for x in range (10,21):
    print(x)


#funciones

#defino las mismas con un def

def saludar():
    print('Hola Mundo!')


def saludar(quien):
    print('hola'+ quien + '!!!')
