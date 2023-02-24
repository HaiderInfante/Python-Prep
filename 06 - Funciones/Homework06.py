#1. Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es
def es_primo (n):
    primo = True
    for i in range (2, n):
        if (n % i == 0):
            primo = False
            break
    return primo

print(es_primo(7))

#2.  Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista
lista1 = list(range(100,301))
lista2 = []

for elemento in lista1:
    if es_primo(elemento):
        lista2.append(elemento)
print(lista2)

#Ahora si quiero crear la funcion:

def crea_lista_primos(lista_valores):
    lista_primos= []
    for elemento in lista_valores:
        if (es_primo(elemento)):
            lista_primos.append(elemento)
    return lista_primos

print(crea_lista_primos(list(range(1,21))))

#3.  Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

def repeat_number(number_list):
    empty_list = [0, 0] 
    for x in number_list:
        cuenta = number_list.count(x)
        if empty_list[1] <= cuenta:
            empty_list.clear()
            empty_list.insert(0, x)
            empty_list.insert(1, cuenta) 
    return f'El numero que mas se repite es {empty_list[0]} y se repite {empty_list[1]} veces'

print(repeat_number([1,1,5,6,8,10,22,5,6,4,11,9,5]))

#LA OTRA FORMA
def valor_modal(lista):
    lista_unicos = []
    lista_repeticiones = []
    if len(lista) == 0:
        return None
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            lista_repeticiones[i] += 1
        else:
            lista_unicos.append(elemento)
            lista_repeticiones.append(1)
    moda = lista_unicos[0]
    maximo = lista_repeticiones[0]
    for i, elemento in enumerate(lista_unicos):
        if lista_repeticiones[i] > maximo:
            moda = lista_unicos[i]
            maximo = lista_repeticiones[i]
    return moda, maximo

lis = [1,1,5,6,8,10,22,5,6,4,11,9,5]
moda, repite = valor_modal(lis)
print('El valor modal es', moda, 'y se repite', repite, 'veces.')

#4.  A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.
def repeat_number(number_list, choose):
    empty_list = [0, 0] 
    for number in number_list:
        count = number_list.count(number)
        if empty_list[0] != number and empty_list[1] == count and choose == 'min':
            if number < empty_list[0]:
                empty_list.clear()
                empty_list.insert(0, number)
                empty_list.insert(1, count)
            else:
                continue                
        elif empty_list[0] != number and empty_list[1] == count and choose == 'max':
            if number > empty_list[0]:
                empty_list.clear()
                empty_list.insert(0, number)
                empty_list.insert(1, count)
            else:
                continue
        elif empty_list[1] < count:
            empty_list.clear()
            empty_list.insert(0, number)
            empty_list.insert(1, count)
    return f'El numero que mas se repite es {empty_list[0]} y se repite {empty_list[1]} veces'

print(repeat_number([1,1,5,5], 'max'))

#LA OTRA FORMA

def valor_modal(lista, menor):
    '''
    Esta función devuelve el valor modal y recibe de parámetros dos valores:
    1-Una lista de números
    2-Verdadero (por defecto) por si se requiere el mínimo de los más repetidos, o Falso si se requiere el máximo
    '''
    lista_unicos = []
    lista_repeticiones = []
    if len(lista) == 0:
        return None
    if (menor):
        lista.sort()
    else:
        lista.sort(reverse=True)
    for elemento in lista:
        if elemento in lista_unicos:
            i = lista_unicos.index(elemento)
            lista_repeticiones[i] += 1
        else:
            lista_unicos.append(elemento)
            lista_repeticiones.append(1)
    moda = lista_unicos[0]
    maximo = lista_repeticiones[0]
    for i, elemento in enumerate(lista_unicos):
        if lista_repeticiones[i] > maximo:
            moda = lista_unicos[i]
            maximo = lista_repeticiones[i]
    return moda, maximo

lis = [10,1,5,6,8,10,22,5,6,4,11,10,9,5]
moda, repite = valor_modal(lis, True)
print('El valor modal es', moda, 'y se repite', repite, 'veces.')

lis = [10,1,5,6,8,10,22,5,6,4,11,10,9,5]
moda, repite = valor_modal(lis, False)
print('El valor modal es', moda, 'y se repite', repite, 'veces.')

# 5. Crear una función que convierta entre grados Celsius, Farenheit y Kelvin
# Fórmula 1 : (°C × 9/5) + 32 = °F
# Fórmula 2 : °C + 273.15 = °K
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
def conversion_grados(valor, origen, destino):
    if (origen == 'celsius'):
        if (destino == 'celsius'):
            valor_destino = valor
        elif (destino == 'farenheit'):
            valor_destino = (valor * 9 / 5) + 32
        elif (destino == 'kelvin'):
            valor_destino = valor + 273.15
        else:
            print('Parámetro de Destino incorrecto')
    elif (origen == 'farenheit'):
        if (destino == 'celsius'):
            valor_destino = (valor - 32) * 5 / 9
        elif (destino == 'farenheit'):
            valor_destino = valor
        elif (destino == 'kelvin'):
            valor_destino = ((valor - 32) * 5 / 9) + 273.15
        else:
            print('Parámetro de Destino incorrecto')
    elif (origen == 'kelvin'):
        if (destino == 'celsius'):
            valor_destino = valor - 273.15
        elif (destino == 'farenheit'):
            valor_destino = ((valor - 273.15) * 9 / 5) + 32
        elif (destino == 'kelvin'):
            valor_destino = valor
        else:
            print('Parámetro de Destino incorrecto')
    else:
        print('Parámetro de Origen incorrecto')
    return valor_destino

print(conversion_grados(3, 'celsius', 'farenheit'))

# 6. Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:
metricas = ['celsius','kelvin','farenheit']
for i in range(0,3):
    for j in range(0,3):
        print('1 grado', metricas[i], 'a', metricas[j],':', conversion_grados(2, metricas[i], metricas[j]))

# 7. Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

def factorial(number):
    if type(number) == float or number < 0 or number == str:
        print("Enter a correct number")
    else:
        count = number
        while count > 1:
            number = number * (count - 1)
            count -= 1
        return number

print(factorial(5))

def factorial(numero):
    if(type(numero) != int):
        return 'El numero debe ser un entero'
    if(numero < 0):
        return 'El numero debe ser pisitivo'
    if (numero > 1):
        numero = numero * factorial(numero - 1)
    return numero
print(factorial(3))
print(factorial(-2))
print(factorial(1.23))
print(factorial('6'))
