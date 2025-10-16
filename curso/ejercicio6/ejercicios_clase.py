# escribir un programa que pida al usuario un numero entero y muestre por pantalla un triangulo
# rectángulo, altura es el numero introducido

print("\n\n\n\nvamos a dibujar un triangulo rectángulo:\n\n\n")
altura = int(input("ingrese la altura: "))


for i in range(altura):
  print("x " * (i + 1))

print("\n\n\n")

# escribir un programa que pida al usuario un numero entero y muestre un cuadrado y un rectangulo
print("ahora vamos a dibujar un cuadrado y un triangulo")

altura = int(input("ingrese las dimensiones del cuadrado: "))
ancho = int(input("ingrese el ancho del rectángulo cuadrado:"))
espaciado = " " * 5
caracter = "x "

# dibujar cuadrado
for i in range(altura):
  print(caracter * altura, espaciado, caracter * ancho)

rectangulo_altura = int(input("ingrese la altura del rectangulo"))
ancho_altura = int(input("ingrese la ancho del rectangulo"))

for i in range(rectangulo_altura):
  print(caracter * ancho_altura)
