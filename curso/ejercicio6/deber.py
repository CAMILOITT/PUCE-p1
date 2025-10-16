# Tarea N 1
# Colocamos un rango de numero de datos, indicar cuantos numero primos están ahi.

separador = "-" * 20
linea_nueva = "\n" * 3

print(linea_nueva)
print(separador, "Contador de números primos.", separador)
inicio = int(input("Indique el inicio del rango: "))
fin = int(input("Indique el final del rango: "))
numero_primos = 0

for i in range(inicio, fin + 1):
  if i > 1:
    for j in range(2, i):
      if (i % j) == 0:
        break
    else:
      numero_primos += 1

print(f"en el rango de {inicio} a {fin} ", f"hay {numero_primos} números primos")

# Tarea N 2
# Dada una frase indicar cuantas vocales y cuantas consonantes.
# ejemplo:
# hola resultado: 2 vocales, 2 consonantes

vocales = ["a", "e", "i", "o", "u"]
n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print(linea_nueva)
print(separador, "Contador de vocales y consonantes", separador)

frase = str(input("Ingrese una frase: ")).lower()
contador_vocales = 0
contador_consonantes = 0

for letra in frase:
  if letra in vocales:
    contador_vocales += 1
  elif letra in n or letra == " ":
    continue
  else:
    contador_consonantes += 1

print(f"La frase tiene {contador_vocales} vocales y {contador_consonantes} consonantes")

print(linea_nueva)
