# Taller2
#   CODEFARMES
![image](https://github.com/LauraDa999/Taller1/assets/141860731/433b1645-87dd-48eb-84d6-fc6bc19051d4)

# 1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).
```
n = int(input("ingrese un numero entero: "))
digitos = []
while n > 0:
    digito = n % 10  # Obtiene el último dígito
    digitos.insert(0, digito)  # Agrega el dígito al principio de la lista
    n = n // 10  # Elimina el último dígito
print("Dígitos separados:")
for digito in digitos:
    print("[" + str(digito) + "]")
```
# EXPLICACION: 
Se le esta solicitando al usuario un número entero y luego separa cada dígito de este número utilizando operaciones de módulo y división entera. Estos dígitos separados se almacenan en una lista y se imprimen en celdas individuales. El bucle extrae los dígitos del número de derecha a izquierda, agregándolos al principio de la lista. Y luego muestra los dígitos separados en celdas mediante un bucle.


# 2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
```
numero_flotante = float(input("Ingrese un número flotante: "))
numero_como_cadena = str(numero_flotante)
parte_entera, parte_decimal = numero_como_cadena.split(".")
print("Dígitos de la parte entera:")
for digito in parte_entera:
    if digito.isdigit():
        print("[" + digito + "]")
print("Dígitos de la parte decimal:")
for digito in parte_decimal:
    if digito.isdigit():
        print("[" + digito + "]")
```
# EXPLICACION:
Se ingresa un número flotante, luego lo convierte  en una cadena para poder manipularlos, luego separa la parte entera y la parte decimal del número utilizando el método split. Después, imprime los dígitos de la parte entera y la parte decimal en celdas individuales, utilizando bucles
La condición isdigit() se usa para asegurarse de imprimir solo los dígitos en lugar de otros caracteres.

# 3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

```
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

cadena1 = str(numero1)
cadena2 = str(numero2)
if cadena1 == cadena1[::-1] and cadena2 == cadena2[::-1]:
    print(f"{numero1} y {numero2} son números espejos.")
else:
    print(f"{numero1} y {numero2} no son números espejos.")
```
# EXPLICACION: 
Este código esencialmente verifica si los números ingresados son iguales a su versión invertida en términos de dígitos.

#  4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
```
import math

def aproximacion_coseno(x, n):
    aproximacion = 0.0

    for i in range(n):
        termino = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
        aproximacion += termino

    return aproximacion

def encontrar_terminos_con_error(x, error):
    n = 0
    valor_real = math.cos(x)
    while True:
        n += 1
        aproximacion = aproximacion_coseno(x, n)
        error_porcentual = abs((aproximacion - valor_real) / valor_real) * 100
        if error_porcentual <= error:
            return n

x = float(input("Ingrese el valor de x: "))

errores = [10, 1, 0.1, 0.01]
for error in errores:
    n_terminos = encontrar_terminos_con_error(x, error)
    print(f"Con un error del {error}%, se necesitan {n_terminos} términos de la serie de Taylor.")
```

# EXPLICACION:
Aqui se esta utilizando la serie de Taylor para aproximar el coseno de un número dado.

#  5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva.

```
#  calcular el MCD
def mcd_iterativo(a, b):
    while b:
        a, b = b, a % b
    return a

# (Mínimo Común Múltiplo) 
def mcm_iterativo(a, b):
    mcd = mcd_iterativo(a, b)
    return a * b // mcd

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

mcm = mcm_iterativo(num1, num2)
print(f"El Mínimo Común Múltiplo de {num1} y {num2} es {mcm}.")
```
# EXPLICACION:
Este  programa solicita al usuario dos números enteros, y luego calcula y muestra el MCM de los números ingresados utilizando el enfoque iterativo.

# 6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in:
```
  elem_unicos = set()
  for elemento in lista:
    if elemento in elem_unicos:
      return True
    elem_unicos.add(elemento)
  return False
entrada = input("escriba una lista de elementos separados por espacios: ")
#convierte los numero de entrada en un lista
elementos = entrada.split()
#aplica la funcion
hay_repetidos = elem_repetidos(elementos)
#imprime los resultados segun la funcion
if hay_repetidos:
  print("La lista contiene elementos repetidos.")
else:
  print("La lista no contiene elementos repetidos.")
```
# EXPLICACION:

#  7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.:
```
  vocales = "a e i o u A E I O U"
  conteo = 0
    if letra in vocales:
      conteo += 1
    #si tiene mas de 2 vocales regresa true 
    if conteo >= 2:
      return True
  return False
entrada = input("escriba cadenas/palabras separadas por espacios: ")
#convierte los datos de entrada en una lista de cadenas.
cadenas = entrada.split()
#imprime la respuesta de todas las cadenas/palabras que cumplan la funcion
print("Cadenas con dos o más vocales en la lista:")
for cadena in cadenas:
  if vocales(cadena):
    print(cadena)
```
# EXPLICACION:

#  8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista:

```

  return [elemento for elemento in lista1 if elemento not in lista2]
#pedir las 2 listas
lista1 = input("escriba la primera lista de elementos separados por espacios: ").split()
lista2 = input("escriba la segunda lista de elementos separados por espacios: ").split()
#se aplica la funcion
no_comunes = elementos(lista1, lista2)
#imprime los elementos no comunes
print("Los lementos de la primera lista que no están en la segunda lista son:")
for elemento in no_comunes:
  print(elemento)
```

# EXPLICACION:

#  9. (Taller 1, punto 7) Resolver el punto 7 del taller 1 usando operaciones con vectores:
```
def calcular_promedio(v, w, x, y, z):
  return (v + w + x + y + z) / 5
```
```
def calcular_mediana(v, w, x, y, z):
  lista = [v, w, x, y, z]
  lista.sort()
  return lista[2]
```
```
def calcular_promedio_multiplicativo(v, w, x, y, z):
  return (v * w * x * y * z) ** (1/5)
 ```
``` 
def orden_ascendente(v, w, x, y, z):
  lista = [v, w, x, y, z]
  lista.sort()
  return lista
 ```
``` 
def orden_descendente(v, w, x, y, z):
  lista = [v, w, x, y, z]
  lista.sort(reverse=True)
  return lista
```
```
def calcular_potencia_mayor_menor(v, w, x, y, z):
  return max(v, w, x, y, z) ** min(v, w, x, y, z)
```
```
def calcular_raiz_cubica_menor(v, w, x, y, z):
  return min(v, w, x, y, z) ** (1/3)
v = float(input("Ingrese el primer número: "))
w = float(input("Ingrese el segundo número: "))
x = float(input("Ingrese el tercer número: "))
y = float(input("Ingrese el cuarto número: "))
z = float(input("Ingrese el quinto número: "))
```
```
prom = calcular_promedio(v, w, x, y, z)
medi = calcular_mediana(v, w, x, y, z)
geo = calcular_promedio_multiplicativo(v, w, x, y, z)
orde = orden_ascendente(v, w, x, y, z)
edro = orden_descendente(v, w, x, y, z)
pot = calcular_potencia_mayor_menor(v, w, x, y, z)
cub = calcular_raiz_cubica_menor(v, w, x, y, z)

print(f"{prom:.5f} es el promedio")
print(f"{medi} es la mediana")
print(f"{geo:.5f} es el promedio multiplicativo")
print(f"{orde} es el orden ascendente")
print(f"{edro} es el orden descendente")
print(f"{pot} es la potencia del mayor elevado por el menor")
print(f"{cub:.5f} es la raíz cúbica del menor")
```

#  10.  Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas

```
    multiplos = []
    for num in lista:
      if num % 3 == 0:
        multiplos.append(num)
    return multiplos
#pedir los numeros separados por espacio y hacer cada valor un dato independiente
entrada = input("Ingresa los valores de la lista separados por espacios: ")
valores = [int(valor) for valor in entrada.split()]
#usa la funcion en la lista creada
multiplos = multiplos_de_tres(valores)
print("Los múltiplos de 3 en la lista son:", multiplos)
```

#  11. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
```
def es_matriz_magica(matriz):
    suma_objetivo = sum(matriz[0])

    for fila in matriz:
        if sum(fila) != suma_objetivo:
            return False

    for j in range(len(matriz)):
        if sum(matriz[i][j] for i in range(len(matriz))) != suma_objetivo:
            return False
    if sum(matriz[i][i] for i in range(len(matriz))) != suma_objetivo:
        return False

    if sum(matriz[i][len(matriz) - i - 1] for i in range(len(matriz))) != suma_objetivo:
        return False

    return True

```
