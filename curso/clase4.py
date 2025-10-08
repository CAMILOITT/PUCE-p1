# # Ejercicio, simulación de un cajero automático.

# print("¡Bienvenido nuevamente!")
# password = "1234"
# password_ingresado = str(input("Ingresar la contraseña:"))
# intentos = 1
# intentos_max = 3

# while intentos < intentos_max:
#   if len(password_ingresado) != 4:
#     print("números de pines incorrectos, numero de intentos disponibles:", abs(intentos - intentos_max))
#     password_ingresado = str(input("Ingrese nuevamente su contraseña: "))
#     intentos += 1
#     continue

#   if password == password_ingresado:
#     valor = int(input("ingrese el valor a retirar:"))
#     print("retirando:", valor)
#     break

#   if intentos == intentos_max:
#     print("tarjeta bloqueada.")
#     break

#   intentos += 1

#   print("contraseña incorrecta, intentos disponibles", intentos)
#   print("inténtalo nuevamente")
#   password_ingresado = str(input("Ingrese nuevamente su contraseña: "))


# # # if a == clave:
# # #   print("Que acción deseas hacer!")
# # # else:
# # #   print("Clave incorrecta: ")

# # if len(a) > 4:
# #   print("ingreso mal la clave")
# # else:
# #   print()


# # len()


# # a = int(input("ingrese su clave:"))
# # clave = 1234
# # if len(a) == 4:
# #   print("digitos correctos")
# # elif a == clave:
# #   print("clave correcta")


if len(a) > 4:
  print("acceso incorrecto")
else:
  print("clave incorrecta")
  a = input("ingrese la calve (intento 2 de 3)")
  if a == clave:
    print("acceso correcto")
  else:
    print("clave incorrecta")
