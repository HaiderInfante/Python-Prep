# 1. Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
lista_ciudades = ['polombia', 'mexico', 'peru', 'Argentina', 'brazil']
print(lista_ciudades)

# 2. Imprimir por pantalla el segundo elemento de la lista
print(lista_ciudades[1])

# 3. Imprimir por pantalla del segundo al cuarto elemento
print(lista_ciudades[1:4])

# 4. Visualizar el tipo de dato de la lista
type(lista_ciudades)
print(type(lista_ciudades))

# 5. Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(lista_ciudades[2:])

# 6. Visualizar los primeros 4 elementos de la lista
print(lista_ciudades[:4])

# 7. Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
lista_ciudades.append('uruguay')
print(lista_ciudades)
lista_ciudades.insert(0, 'polombia')
print(lista_ciudades)

# 8. Agregar otra ciudad, pero en la cuarta posición
lista_ciudades.insert(3, 'japon')
print(lista_ciudades)

# 9. Concatenar otra lista a la ya creada
lista_ciudades2 = ['inglaterra']
lista_ciudades.extend(lista_ciudades2)
print(lista_ciudades)

# 10. Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
print(lista_ciudades.index('polombia'))

# 11. ¿Qué pasa si se busca un elemento que no existe?
#print(lista_ciudades.index('colombia'))
if ('paris' in lista_ciudades):
    print(lista_ciudades.index('paris'))

# 12. Eliminar un elemento de la lista
lista_ciudades.remove('inglaterra')
print(lista_ciudades)

# 13. ¿Qué pasa si el elemento a eliminar no existe?
#lista_ciudades.remove('englaterra')

# 14. Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
last = lista_ciudades.pop()
print(last)
# 15. Mostrar la lista multiplicada por 4
print(lista_ciudades * 4)

# 16. Crear una tupla que contenga los números enteros del 1 al 20
tupla = tuple(range(1, 21))
print(tupla)

# 17. Imprimir desde el índice 10 al 15 de la tupla
print(tupla[10:15])

# 18. Evaluar si los números 20 y 30 están dentro de la tupla
print(20 in tupla)
print(30 in tupla)

# 19. Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
# if ('paris' in tupla):
#     print('el dato existe')
# else:
#     agregar = tupla.append('paris')
#     print(tupla)


# 20. Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print(tupla.count(1))
print(lista_ciudades.count('polombia'))

# 21. Convertir la tupla en una lista
mylist2 = list(tupla)
print(mylist2)

# 22. Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
#desempaquetar: me los convierte a variables
v1, v2, v3, v4  = tupla[0:4]
print(v1)
print(v2)
print(v3)
print(v4)
#empaquetar
tup2 = (v1, v2, v3, v4)
print(tup2)

# 23. Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
mydictionary = {
    'city': ['bogota', 'lima'],
    #'country': ['polombia', 'mexico', 'peru', 'Argentina', 'brazil'],
    'country': lista_ciudades,
    'continent': ['america', 'asia', 'europa']
}
print(mydictionary)

# 24. Imprimir las claves del diccionario
print(mydictionary.keys())
print(mydictionary.values())

# 25. Imprimir las ciudades a través de su clave
print(mydictionary['city'])