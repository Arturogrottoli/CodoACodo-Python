#metodo _init_ exclusivo de python

#Ejemplo

class Empleado:

  def _init_(self):
    self.nombre=input("Ingrese el nombre del empleado:")
    self.sueldo=float(input("Ingrese el sueldo:"))

  def imprmir(self):
    print("Nombre:", self.nombre)
    print("Sueldo:", self.sueldo)

  def paga_impuestos(self):
      if self.sueldo>5000:
        print("debe pagar impuestos")
      else:
        print("no debe pagar impuestos")

#bloque principal

empleado1=Empleado()
empleado1.imprmir()
empleado1.paga_impuestos()