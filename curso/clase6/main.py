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

MES_ACTUAL = 10
ANO_ACTUAL = 2025
DIA_ACTUAL = 21
PROMEDIO_DIAS_MES = 30
MESES_EN_ANO = 12

print(" " * 5, "Calculadora de edad", " " * 5)
print("-" * 30)
print("Ingrese los siguientes datos de su fecha de nacimiento:")
dia_usuario_nacimiento = int(input("Dia (1-30): "))
mes_usuario_nacimiento = int(input("Mes (1-12): "))
ano_usuario_nacimiento = int(input("Año: "))

contador_ano = 0
contador_mes = 0
contador_dia = 0

# Ajuste de días y meses
if dia_usuario_nacimiento > DIA_ACTUAL:
  DIA_ACTUAL += PROMEDIO_DIAS_MES
  MES_ACTUAL -= 1
if mes_usuario_nacimiento > MES_ACTUAL:
  MES_ACTUAL += MESES_EN_ANO
  ANO_ACTUAL -= 1

CONDICION_WHILE = (
  ano_usuario_nacimiento < ANO_ACTUAL or mes_usuario_nacimiento < MES_ACTUAL or dia_usuario_nacimiento < DIA_ACTUAL
)

while CONDICION_WHILE:
  if ano_usuario_nacimiento < ANO_ACTUAL:
    ano_usuario_nacimiento += 1
    contador_ano += 1
  if mes_usuario_nacimiento < MES_ACTUAL:
    contador_mes += 1
    mes_usuario_nacimiento += 1
  if dia_usuario_nacimiento < DIA_ACTUAL:
    contador_dia += 1
    dia_usuario_nacimiento += 1


print("Tu fecha de nacimiento es")
print("tienes:", contador_ano, "años, con", contador_mes, "meses y", contador_dia, "dias.")
