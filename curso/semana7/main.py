# cadena = input("Ingrese una cadena: ")
# subcadena = str(input("Ingrese una subcadena: "))

# if cadena.startswith (subcadena):
#   print(f"La cadena empieza con la subcadena '{cadena}'.")
# else:
#   print(f"La cadena NO empieza con la subcadena '{cadena}'.")

# Ejercicio 2

# cadena = str(input("Ingrese una cadena: "))

# for caracter in cadena:
#   print(caracter)

# Ejercicio 3

# cadena = str(input("Ingrese una cadena: "))

# while True:
#   caracter = str(input("Ingrese un caracter: "))

#   if len(caracter) == 1:
#     break

# print("En la cadena:", caracter, "se encuentra", cadena.count(caracter), "veces el caracter", caracter)


# Ejercicio 4

txt = str(input("Ingrese una oracion: "))

arr_txt = txt.split()
print(len(arr_txt))