# escribir un programa que pida al usuario un numero entero y muestre por pantalla un triangulo
# rectángulo, altura es el numero introducido

print("vamos a dibujar un triangulo rectángulo: ")
altura = int(input("ingrese la altura"))


for i in range(altura):
  print("x " * (i + 1))


# escribir un programa que pida al usuario un numero entero y muestre un cuadrado y un rectangulo
print("ahora vamos a dibujar un cuadrado y un triangulo")

altura = int(input("ingrese las dimensiones del cuadrado: "))
ancho = int(input("ingrese el ancho del triangulo cuadrado: "))
espaciado = " " * 5
caracter = "X " * altura

# dibujar cuadrado
for i in range(altura):
  print(caracter, espaciado, caracter)
