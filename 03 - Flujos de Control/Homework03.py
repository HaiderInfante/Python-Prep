primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
print(primos[3:10])
# 1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

variable = 2

if variable > 0:
    print("Es mayor a cero")

else:
    print("Es menor a cero")

# 2. Crear dos variables y un condicional que informe si son del mismo tipo de dato
variable_01 = 'Hola'
variable_02 = 2

if type(variable_01) == type(variable_02):
    print("Son del mismo tipo de dato")
else:
    print("No son del mismo tipo de dato")

# 3. Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for n in range(1, 21):
    if n % 2 == 0:
        print(f'El numero {n} es par')
    else:
        print(f'El numero {n} es impar')

# 4. En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for n in range(0, 6):
    print(f'El numero {n} elevado a la potencia 3 es igual a: {n**3}')

# 5. Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
variable = 5

for n in range (1, 6):
    print(f'Este es el ciclo numero {n}')

# 6. Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

#primera forma
factor = 4
count = 4

while count > 1:
    factor = factor * (count - 1)
    count -= 1
print(factor)

numero = 4
factorial = 1
while(numero > 1):
    factorial = numero * factorial
    numero = numero - 1
print(factorial)

# 7. Crear un ciclo for dentro de un ciclo while 

count = 0

while count < 5:
    print(f'Este es el ciclo numero {count} del while')
    for i in range (0, 5):
        print(f'Este es el ciclo numero {i} del for')
    count += 1

# 8. Crear un ciclo while dentro de un ciclo for
for i in range (0, 5):
    print(f'Este es el ciclo numero {i} del FOR')
    count = 0
    while count < 5:
        print(f'Este es el ciclo numero {count} del WHILE')
        count += 1

m = 5
for i in range(1, m):
    n = 5
    while(n > 1):
        print('Ciclo while nro ' + str(n))
        print('Ciclo for nro ' + str(i))        
        n -= 1

# 9. Imprimir los números primos existentes entre 0 y 30
tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
 

# 10. ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin


# 11. En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# 12. Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# 13. Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
count = 100
while count <= 300:
    if count % 12 != 0:
        count += 1
        continue
    
    print(count)
    count += 1

# 14. Utilizar la función input() que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente


# 15. Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
count = 100
while count <= 300:
    if count % 6 == 0:
        print(count)
        break
    count += 1