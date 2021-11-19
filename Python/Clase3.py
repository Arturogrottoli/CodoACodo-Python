#Tuplas y diccionarios

#1 Definir tuplas e imprimir sus elementos

tupla=(1, 2, 3)
fecha=(25, "diciembre", 2021)
persona=("Juan", "Carlos")

print(tupla)
print(fecha)
print(persona)

#2 Desarrollar una funcion que solicite la carga de dia, mes y año y almacene los datos en una tupla que debe retornar, la segunda debe recibir una tupla con la fecha y mostrarla por pantalla

def carga_fecha():
  dd=int(input("Ingrese el numero del dia:"))
  mm=int(input("Ingrese el numero del mes:"))
  aa=int(input("Ingrese el numero del año:"))
  tuplaFecha = (dd,mm,aa)
  return tuplaFecha

def mostrar_fecha (fecha):
  print(fecha [0],fecha [1],fecha [2], sep="/")

fecha=carga_fecha()
mostrar_fecha(fecha)

#ordenamiento Sorted, me ordena el array o tupla por letra o num

numeros=[1,5,3,8]
print(sorted(numeros))


#Listas tratadas como objetos

#append (agrego un elemento al final) se usa para cuando es uno solo a agregar

lista=('Juan','Carlos','Batman')
lista.append('Culo')
print(lista)

#insert (Posicion, elemento) lo colocamos en la posicion que queremos

lista1=('Juan','Carlos','Batman')
lista1.append(1,'Culo')   #Juan culo carlos batman
print(lista1)

#pop borra ultimo elemento

elemento=lista.pop()

#tambien se puede usar como posicion

#remove(elemento) borra el elemento que indiquemos

#Count, cuenta cuantas veces está un elemento

print(lista.count('Juan'))  #daria 1

#sort ordena y reverse ordena al reves (por numero o por inicial de letra)

#DICCIONARIOS tienen { } en vez de ( ) o []

productos = {
               'azucar':20,
               'yerba':30,
               'cafe':40,
}

print(productos)
print('La cantidad de elementos del diccionario es', len(productos))
print('El precio de la yerba es ', '$', productos['yerba'])


#Desarrollar un programa que cargue los lados de un triangulo e implemente los siguiente metodos : inicializar los atriobutos, imprimir el valor  del lado mayor y otro emtodo que diga si es equilatero o no. La clase se llamara Triangulo

class Triangulo:
  def inicializar(self):
    self.lado1=int(input("Ingrese lado 1:"))
    self.lado2=int(input("Ingrese lado 2:"))
    self.lado3=int(input("Ingrese lado 3:"))

  def imprimir(self):
    print("Los valores de los lados del triangulo son:")
    print("Lado 1:",self.lado1)
    print("Lado 2:",self.lado2)
    print("Lado 3:",self.lado3)

  def lado_mayor(self):
    print("Lado mayor:")
    if self.lado1>self.lado2 and self.lado1>self.lado3:
        print(self.lado1)
    else:
      if self.lado2>self.lado3:
        print(self.lado2)
      else:
        print(self.lado3)

  def es_equilatero(self):
     if self.lado1==self.lado2 and self.lado1==self.lado3:
       print("El triangulo es equilatero")
     else:
       print("El triangulo no es equilatero")
 
 #definicion
 
triangulo1=Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.es_equilatero()
  