print("Ejercicio 1")
#Funcion que le damos un lado de un cuadrado y nos retorna su superficie

def supcuadrado(lado):
    sup=lado*lado
    return sup

va=int(input("Ingrese el valor del lado del cuadrado:"))
superficie=(supcuadrado(va))
print("La superficie del cuadrado es ",superficie)

#Ejercicio largo de caracteres

def largo(cadena):
    return len(cadena)

nombre1=input("Ingrese el primer nombre:")
nombre2=input("Ingrese el segundo nombre:")

lar1=largo(nombre1)
lar2=largo(nombre2)

if lar1==lar2:
    print("Los nombres", nombre1,nombre2, "tienen igual cantidad de letras")

else:
     if lar1<lar2:
        print(nombre2 ,"es mas largo")
     else:
        print(nombre1 ,"es mas largo")

#Ejercicio
#ingresar ancho y alto de un rectangulo, calcular area

def area(ancho,alto):
    print("Area del rectangulo es:", ancho*alto)

ancho=int(input("Ingrese el ancho del rectangulo:"))
alto=int(input("Ingrese el alto del rectangulo:"))

area(ancho,alto)


#tuplas

tupla1=(1,2,3,4)
print(tupla1)

print('Contenido de la posicion 2', tupla1[2])

#Ejercicio 5

lista = []

for j in range(5):
    numero = int(input("Ingrese numero:"))
    lista.append(numero)

for y in range(5):
    if lista[y]>=7:
        print(list[y])

print("---------------------------")



