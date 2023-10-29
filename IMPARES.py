1
n = int(input("ingrese un numero entero: "))
digitos = []
while n > 0:
    digito = n % 10  # Obtiene el último dígito
    digitos.insert(0, digito)  # Agrega el dígito al principio de la lista
    n = n // 10  # Elimina el último dígito
print("Dígitos separados:")
for digito in digitos:
    print("[" + str(digito) + "]")



3
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

cadena1 = str(numero1)
cadena2 = str(numero2)
if cadena1 == cadena1[::-1] and cadena2 == cadena2[::-1]:
    print(f"{numero1} y {numero2} son números espejos.")
else:
    print(f"{numero1} y {numero2} no son números espejos.")


5

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




7
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

9
def calcular_promedio(v, w, x, y, z):
  return (v + w + x + y + z) / 5

def calcular_mediana(v, w, x, y, z):
  lista = [v, w, x, y, z]
  lista.sort()
  return lista[2]

def calcular_promedio_multiplicativo(v, w, x, y, z):
  return (v * w * x * y * z) ** (1/5)

def orden_ascendente(v, w, x, y, z):
  lista = [v, w, x, y, z]
  lista.sort()
  return lista

def orden_descendente(v, w, x, y, z):
  lista = [v, w, x, y, z]
  lista.sort(reverse=True)
  return lista

def calcular_potencia_mayor_menor(v, w, x, y, z):
  return max(v, w, x, y, z) ** min(v, w, x, y, z)

def calcular_raiz_cubica_menor(v, w, x, y, z):
  return min(v, w, x, y, z) ** (1/3)
v = float(input("Ingrese el primer número: "))
w = float(input("Ingrese el segundo número: "))
x = float(input("Ingrese el tercer número: "))
y = float(input("Ingrese el cuarto número: "))
z = float(input("Ingrese el quinto número: "))

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


11
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

