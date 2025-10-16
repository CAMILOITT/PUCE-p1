# Contabilizar cuantos numeros son pares e impares.


inicio = int(input("inicio del rango"))
fin = int(input("fin del rango"))
pares = 0
impares = 0

for i in range(inicio, fin + 1):
  if i % 2 == 0:
    pares += 1
  else:
    impares += 1

print(f"el rango de {inicio} a {fin}: ")
print("la cantidad de numeros pares: ", pares)
print("la cantidad de numeros impares: ", pares)
