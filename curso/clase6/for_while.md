# conceptos bucle

## For

```python

for i in range(10):
  print(i) # Resultados: 0, 1, 2,..., 9

```

### Características

- Tiene un inicio y un fin.
- Va de un rango a otro.
- tiene posición y ubicación.
- No tiene contadores por que ya tiene un rango.

La ubicación va a ser los indices dada por la maquina, es decir empieza por 0,
mientras que la posición es la ubicación que le damos como humanos, empieza desde 1.

#### Ejemplo

```python
por la maquina  123456 # <-- POSICIÓN
               "prueba"
por el humano   012345 # <-- UBICACIÓN
```

## While

Es utilizada para hacer un loop infinito.

```python
edad = 17

while edad <= 20: 
  print("Ejecutándose") # Se ejecuta mientras no se cumpla la condición.
  edad += 1
```

### Características

- Debe de cumplir una condición, (si no la cumple se vuelve un lazo infinito).
- Se ejecuta mientra que la condición cumpla.
- Esta relacionado con el if.
- Se necesita un contadora para saber cuantas veces se ejecuto el bucle.
