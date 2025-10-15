# print("iterando entre un rango de datos")

# num_iteracion = int(input("Ingrese el numero de datos, que deseas repetir"))

# for i in range(num_iteracion, 2):
#   print("los datos son:", i + 1)

# num_iteracion = int(input("Ingrese el numero de datos, que deseas repetir: "))

# ubicación desde 0 y posición desde 1
#  en la function range el numero, va desde hasta el numero -1
# en la funcion range cuando se tiene 3 datos el ultimo es el salto de la cantidad que se indica

# for i in range(num_iteracion, 20, 2):
#   print("los datos son:", i)
# Iterando sobre una cadena
# text = str(input("ingrese un texto:\n"))

# for char in text:
#   print("imprime caracter", char)


# Iterando sobre una lista
# for v in [10, 5, 3, 4]:
#   print("valor de la lista", v)

num = int(input("en que ubicación deseamos parar."))

for i in range(1, 15):
  if i == num:
    continue
  print("el numero es:", i)

  if i == 11:
    break
