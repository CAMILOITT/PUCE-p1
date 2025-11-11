# Ejercicios while
# contador = 0

# while contador <= 5:
#   print("El valor de contador es:", contador)
#   contador += 1

# print("El bucle del while termino")

# numero = 0
# while numero <= 10:
#   numero += 1
#   if numero == 5:
#     continue
#   if numero == 8:
#     break

#   print("El valor de numero es:", numero)

# print("El bucle del while termino")

# limite = int(input("Ingrese un numero final: "))
# contador = 1

# while contador <= limite:
#   print("El contador es:", contador)
#   contador += 1

# print("El bucle del while termino")
# import numpy

# * Contador de while, por que se acumula la info
# suma_total = 0

# * Condición de while, ya que se utiliza en la condición de while
# numero = 0
# print("Ingrese los números positivos para sumarlos: ")

# while numero >= 0:
#   numero = float(input("Ingrese un numero: "))
#   if numero >= 0:
#     suma_total += numero

# print("La suma total es:", suma_total)

# ! Ejercicio 4
# * CONTADOR: num
# limite = int(input("Ingresé un limite: "))
# num = 2

# while num <= limite:
#   print(num)
#   num += 2

# print("El bucle termino")

# Ejercicio 5
# num = int(input("Ingrese un numero final: "))

# factorial = 1
# i = 1

# while i <= num:
#   factorial *= i
#   i += 1

# print("El factorial de", num, "es:", factorial)


# Ejercicio en clase

# ingresar la fecha de cumpleaños del usuario y mostrar cuantos año, meses y Dias tiene.

ano_actual = 2025
mes_actual = 10
dia_actual = 22

ano_usuario_nacimiento = int(input("Ingrese su año de nacimiento: "))
mes_usuario_nacimiento = int(input("Ingrese su mes de nacimiento (1-12): "))
dia_usuario_nacimiento = int(input("Ingrese su dia de nacimiento: (1-30): "))

contador_ano = 0
contador_mes = 0
contador_dia = 0

if dia_usuario_nacimiento > dia_actual:
  dia_actual += 30
  mes_usuario_nacimiento += 1
if mes_usuario_nacimiento > mes_actual:
  mes_actual += 12
  dia_usuario_nacimiento += 1

while ano_usuario_nacimiento < ano_actual and mes_usuario_nacimiento <= mes_actual:
  if ano_usuario_nacimiento < ano_actual:
    ano_usuario_nacimiento += 1
    contador_ano += 1
  if mes_usuario_nacimiento < mes_actual:
    contador_dia += 1
    mes_usuario_nacimiento += 1
  if dia_usuario_nacimiento < dia_actual:
    contador_dia += 1
    dia_usuario_nacimiento += 1

print("tienes", contador_ano, "años, con", contador_mes, "meses y", contador_dia, "dias")
