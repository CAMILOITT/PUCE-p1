# Trabajando con caracteres en python

## Introducción

Los STRINGS son una secuencia de características utilizadas para representa un texto. Se definen por comillas simples o dobles.

```py
a = "hola mundo"
print(a) # Output: hola mundo
```

## Creación y manipulación de caracteres

Para crear una variable de tipo string, utilizamos las comillas simples o dobles. Otra forma de crear string es utilizar la función str().

```py
# Opción 1
a = "hola mundo"
print(a) # Output: hola mundo

# Opción 2
a = str("hola mundo")
print(a) # Output: hola mundo
```

### Manipulación de caracteres

Los caracteres se puede manipular de diferentes maneras.

```py
# Extracción de datos.

a = "hola mundo"
print(a[0]) # Output: h
print(a[1]) # Output: o
print(a[2]) # Output: l
print(a[3]) # Output: a

# Concatenación de caracteres.

a = "hola"
b = "mundo"
print(a + b) # Output: hol

# obtención de un rango de datos.

a = "hola mundo"
print(a[0:4]) # Output: hola
print(a[5:9]) # Output: mundo

```

## Declaración y Asignación

Para declarar una variable string se lo puede hacer como cualquier otro tipo de dato, es decir:

```py
# declaro una variable llamada, paso siguiente creamos el texto que desamos entre comillas.
a = "hola mundo"
print(a) # Output: hola mundo
```

## Funciones con strings

Python nos provee algunas funciones para trabajar con strings.

### Join

Nos permite unir 2 o más strings, mediante un separador. **Solo se puede utilizar con lista de datos en tipo string**

```py
a= "hola"
b="mundo"
separador=", "

print(separador.join([a,b])) # Output: hola, mundo

# lista de hobbies favoritos
hobbies_favoritos = ["videojuegos", "películas", "dibujar", "pintar"]
print("Mis hobbies favoritos son: ",separado.join(hobbies_favoritos)) # Output: Mis hobbies favoritos son: videojuegos, películas, dibujar, pintar
```

## Código ascii

El código ascci son un sistema de codificación las cuales se encarga de representar caracteres mediante código.

Algunos ejemplos en windows tenemos:

|código|carácter|
|---|---|
|alt + 40| ( |
|alt + 41| ) |
|alt + 42| * |
|alt + 43| + |

## Posiciones y ubicaciones en strings

### La Posición

La posicion se refiere a un punto especifico dentro de un dato

### Ubicación

Se suele referir a la ubicación en memoria la cual tienen el string

```py
nombre = "Catalina"

# en el caso de catalina tenemos que la posición va a empezar desde 1 es decir

# 1 2 3 4 5 6 7 8
# C a t a l i n a

# mientras que si lo vemos desde la ubicacion tenemos que empezar desde 0

# 0 1 2 3 4 5 6 7
# C a t a l i n a

```

## Indexación 

La indexación nos permite obtener el valor de un caracter en una ubicacion especifica.Por lo tanto lo podemos ingresar de la siguiente manera:

```py
nombre= "Anamaria"

# ingresar a un valor en especifico
print(nombre[0]) # Output: A
print(nombre[1]) # Output: n


# Errores que puede ocurrir

# Al ingresar a una posicion que no existe
print(nombre[14]) # Output: IndexError: string index out of range


# Se puede obtener también con números negativos
print(nombre[-1]) # Output: a
print(nombre[-2]) # Output: r

# obtener cierta parte del string
print(nombre[0:3]) # Output: Ana
print(nombre[4:9]) # Output: mari

# si en ele tamaño ponemos un valor mas grande que el tamaño del string, simplemente imprime hasta el final
print(nombre[:40]) # Output: Anamaria


# tambien se puede obtener hasta el final del string de una forma facil
print(nombre[4:]) # Output: maria
print(nombre[-5:]) # Output: maria

# Tambien podemos obtener valores del string saltan algunos indices
# string[inicio:fin:salto]
print(nombre[::5]) # Output: Ar
print(nombre[::2]) # Output: Aaai

# también lo podemos de hacer con saltos negativos
print(nombre[-1::-2]) # Output: armn
```

## Casting

### Cadena a Numeros

Python no permite hacer la conversion de números a fechas, sin embargo esto solo funciona si el string tienen números, si el string contiene letras o caracteres alfanuméricos especiales, simplemente va a salir un error.

```py

# Correcta forma de castear un string a un número

txt = "5294"

print(int(txt)) # Output: 5294
print(float(txt)) # Output: 5294.0

# Errores que podemos tener

txt = "prueba"

print(int(txt)) # Output: ValueError: invalid literal for int() with base 10: ''
print(float(txt)) # Output: ValueError: could not convert string to float: ''

```

### Cadena a Fecha

Existe varios formatos de fecha que tenemos y lo podemos utilizar para indicar el dia

```py
# Formato: dd/mm/aaaa
fecha = "11/05/2002"

# Formato: aaaa/mm/dd
fecha2 = "2002/05/33"

# Formato: mm/dd
fecha3 = "05/2"
```
