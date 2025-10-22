# x = int(input("Ingresa un numero final: "))

# while x > 0:
#   x -= 1
#   print(x)

# i = 1

# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# i = 1

# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


# * Si funciona esta estructura, el ';' actúa como separador.
# i = 0
# while i < 6: i += 1 ; print(i)
# z = 7
# x = 1

# while z > 0:
#   print(" " * z, "*" * x, " " * z)
#   z -= 1
#   x += 2


# text = "Python"
# i = 0
# while i < len(text):
#   print(text[: i + 1])
#   i += 1

# number = int(input("Ingrese un numero: "))
# final = int(input("Ingrese un numero final: "))

# while number < final:
#   if number % 2 == 0:
#     print("el numero", number, "es par")
#   else:
#     print("el numero", number, "es impar")
#   number += 1


# print("Escriba si para continuar")

# respuesta = input("Desea continuar en el programa: ")

# while respuesta == "si":
#   respuesta = input("Desea continuar en el programa: ")

# print("hasta luego.")

# serie de Fibonacci

a, b = 0, 1
num = int(input("Ingrese un numero para la serie de Fibonacci: "))

while b < num:
  print(b)
  a, b = b, a + b
