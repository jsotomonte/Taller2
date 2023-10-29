# Taller2
#   CODEFARMES
![image](https://github.com/LauraDa999/Taller1/assets/141860731/433b1645-87dd-48eb-84d6-fc6bc19051d4)

# 1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).
```
# Solicita al usuario que ingrese un número entero
n = int(input("ingrese un numero entero: "))

# Inicializa una lista para almacenar los dígitos separados
digitos = []

# Separa los dígitos utilizando operadores de módulo y división entera
while n > 0:
    digito = n % 10  # Obtiene el último dígito
    digitos.insert(0, digito)  # Agrega el dígito al principio de la lista
    n = n // 10  # Elimina el último dígito

# Imprime los dígitos separados en celdas
print("Dígitos separados:")
for digito in digitos:
    print("[" + str(digito) + "]")
```
# 2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
```
# Solicita al usuario que ingrese un número flotante
numero_flotante = float(input("Ingrese un número flotante: "))

# Convierte el número a una cadena para trabajar con los dígitos
numero_como_cadena = str(numero_flotante)

# Separa la parte entera y la parte decimal
parte_entera, parte_decimal = numero_como_cadena.split(".")

# Imprime los dígitos de la parte entera en celdas
print("Dígitos de la parte entera:")
for digito in parte_entera:
    if digito.isdigit():
        print("[" + digito + "]")

# Imprime los dígitos de la parte decimal en celdas
print("Dígitos de la parte decimal:")
for digito in parte_decimal:
    if digito.isdigit():
        print("[" + digito + "]")
```

# 3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

```
# Solicita al usuario que ingrese dos números enteros
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

# Convierte los números a cadenas
cadena1 = str(numero1)
cadena2 = str(numero2)

# Compara las cadenas originales con sus versiones invertidas
if cadena1 == cadena1[::-1] and cadena2 == cadena2[::-1]:
    print(f"{numero1} y {numero2} son números espejos.")
else:
    print(f"{numero1} y {numero2} no son números espejos.")
```

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
#  5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva.

```
# Función iterativa para calcular el MCD (Máximo Común Divisor)
def mcd_iterativo(a, b):
    while b:
        a, b = b, a % b
    return a

# Función para calcular el MCM (Mínimo Común Múltiplo) utilizando el MCD
def mcm_iterativo(a, b):
    mcd = mcd_iterativo(a, b)
    return a * b // mcd

# Solicitar al usuario ingresar dos números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# Calcular y mostrar el MCM utilizando el enfoque iterativo
mcm = mcm_iterativo(num1, num2)
print(f"El Mínimo Común Múltiplo de {num1} y {num2} es {mcm}.")
```

# 6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in:
