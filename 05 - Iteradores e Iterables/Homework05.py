# #Ejercicios en clase

# lista = [5, 4, 9, 2]
# i = 0
# while i < len(lista):
#     elemento = lista [i]
#     print(elemento)
#     i += 1

# for elemento in lista:
#     print(elemento)

# cadena = 'Hola'
# for c in cadena:
#     print(c)

# cadena = 'hola'
# for i, c in enumerate(cadena):
#     print(i,c)

# from collections import Iterable

# cadena = 'hola'
# numero = 3
# print(isinstance(cadena, Iterable))
# print(isinstance(numero, Iterable))

# print(list('haider'))
# print(sum([1, 2, 3]))
# print('-'.join('hola'))

# mi_dict = {'a': 1, 'b': 2, 'c': 3}
# for i in mi_dict: #Arroja las claves
#     print(i)

# libro = ['pagina1', 'pagina2', 'pagina3', 'pagina4']
# marcapaginas = iter(libro)
# print(next(marcapaginas))
# print(next(marcapaginas))
# print(next(marcapaginas))
# print(next(marcapaginas))
# #si vuelvo a acceder a otro elemento me va a saltar la excepcion stopoteracion ya que hemos llegado al final.
# print(next(marcapaginas))

# a = [1, 2]
# b = ['uno', 'dos']
# c = zip (a, b)
# print(type(c))
# print(list(c))

# frase = 'el perro de san roque no tiene rabo'
# erres = [i for i in frase if i == 'r']
# print(erres)
# print(len(erres))




#EJERCICIOS DE TAREA

# 1. A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

lista = []
i = -15
while i <= -1:
    lista.append(i)
    i += 1
print(lista)

list2 = list(range(-15, 0))
print(list2)

# 2. ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
i = 0
while i < len(lista):
    elemento = lista[i]
    if elemento % 2 == 0:
        print(elemento)
    i += 1

# 3. Resolver el punto anterior sin utilizar un ciclo while
for elemento in lista:
    if elemento % 2 == 0:
        print(elemento)

# 4. Utilizar el iterable para recorrer sólo los primeros 3 elementos
contador = 0
for elemento in lista:
    if contador > 2:
        break
    print(elemento)
    contador += 1

#otra forma
for elemento in lista [:3]:
    print(elemento)

# 5. Utilizar la función enumerate para obtener dentro del iterable, tambien el índice al que corresponde el elemento
for i, c in enumerate(lista):
    print(i, c)

# 6. Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]
lista2 = [1,2,5,7,8,10,13,14,15,17,20]

for i in range (1, 21):
    if i not in lista2:
        lista2.append(i)

lista2.sort()
print(lista2)

#otra forma:
n = 1
while(n <= 20):
    if (not(n in lista2)):
        lista2.insert((n-1), n)
    n += 1
print(lista2)

# 7. La sucesión de Fibonacci es un listado de números que sigue la fórmula:
# n0 = 0
# n1 = 1
# ni = ni-1 + ni-2
# Crear una lista con los primeros treinta números de la sucesión.
fibo = [0, 1]
n = 2
while n < 30:
    fibo.append(fibo[n-1] + fibo[n-2])
    n += 1
print(fibo)
#R//514229

# 8. Realizar la suma de todos elementos de la lista del punto anterior
suma = 0
for elemento in fibo:
    suma += elemento
print(suma)
#lo mas facil
sum(fibo)

# 9. La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:
# Donde i es la cantidad total de elementos
# ni-1 / ni
# ni-2 / ni-1
# ni-3 / ni-2
# ni-4 / ni-3
# ni-5 / ni-4

n = 2
while n < 7:
    divition = fibo[n] / fibo[n-1] 
    print(divition)
    n += 1

# 10. A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
cadena = 'hola mundo'
for i, c in enumerate (cadena):
    if c == 'n':
        print(i)

# 11. Crear un diccionario e imprimir sus claves utilizando un iterador
my_dict = {
    'pais': 'colombia',
    'capital': 'bogota'
}

for i in my_dict:
    print(i)

# 12. Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador
print(list(cadena))

for i in cadena:
    print(i)

marcahojas = iter(cadena)
print(next(marcahojas))
print(next(marcahojas))
print(next(marcahojas))
print(next(marcahojas))

#otra formar
recorre = iter(cadena)
largo = len(cadena)
for i in range (0, largo):
    print(next(recorre))

# 13. Crear dos listas y unirlas en una tupla utilizando la función zip
list1 = ['ciencia', 'ciclismo', 'leer']
list2 = ['haider', 'monica', 'anderson']
list3 = zip(list1, list2)
print(list(list3))

# 14. A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
newlis = [i for i in lis if i % 7 == 0]
print(newlis)

# 15. A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

lis2 = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
print(len(lis2))
print('2do ejemplo')
for elementos in lis2:
    print(len(elementos))

#la formar correcta

cantidad = 0
for elemento in lis2:
    if (type(elemento) == list):
        cantidad += len(elemento)
    else:
        cantidad += 1
print ('la cantidad total de elementos es: ', cantidad)

# 16. Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
lis2 = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
for elemento in lis2:
    if elemento == str:
        elemento = list(elemento)
        lis2.append(elemento)
print(lis2)

#correcion
for indice, elemento in enumerate(lis2):
    if (type(elemento) != list):
        lis2[indice] = [elemento]
print(lis2)