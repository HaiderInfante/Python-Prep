# mi_variable = 12
# print(mi_variable)

# mi_variable2 = 'dario'
# print(mi_variable2)

# mi_complejo = 5 + 7j
# print(mi_complejo)


# mi_numero = input('Ingrese un valor')
# print('el valor ingresado fue', mi_numero)

#EJERCICIOS HOMEWORK02

# 1. Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
variable1 = 5
print(variable1)

# 2. Imprimir el tipo de dato de la constante 8.5
variable2 = 8.5
print(type(variable2))

# 3. Imprimir el tipo de dato de la variable creada en el punto 1
print(type(variable1))

# 4. Crear una variable que contenga tu nombre
variable3 = "Haider Infante"

# 5. Crear una variable que contenga un número complejo
variable4 = 1 + 1j

# 6. Mostrar el tipo de dato de la variable crada en el punto 5
print(type(variable4))

# 7. Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
variable5 = 3.1416

# 8. Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
variable6 = 'True'
variable7 = True
#No es lo mismo la primera es una variable tipo string y la otra variable es tipo booleano

# 9. Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(f'La variable 1 es de tipo: {type(variable6)} y la variable 2 es de tipo: {type(variable7)}')


# 10. Asignar a una variable, la suma de un número entero y otro decimal
variable8 = 8 + 5.8
print(variable8)

# 11. Realizar una operación de suma de números complejos
variable9 = 1 + 1j
variable10 = 2 + 2j
print(variable9 + variable10)

# 12. Realizar una operación de suma de un número real y otro complejo
variable11 = 1.1
variable12 = 1 + 1j
print(variable11 + variable12)

# 13. Realizar una operación de multiplicación
print(3 * 4)

# 14. Mostrar el resultado de elevar 2 a la octava potencia
print(2 ** 8)

# 15. Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
variable13 = 27/4
print(variable13)

# 16. De la división anterior solamente mostrar la parte entera
variable13 = 27//4
print(variable13)

# 17. De la división de 27 entre 4 mostrar solamente el resto
print(27 % 4)

# 18. Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(6 * 4 + 3)

# 19. Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
a = 'Haider'
b = 'Andrés' 
print(f'{a} {b}')

# 20. Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print(2 == "2")

# 21. Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(2 == int('2'))

# 22. ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# var1 = float('3,8')
# print(var1)
# No se puede convertir un entero a un float

# 23. Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
var2 = 3
var2 -= 5
print(var2)

# 24. Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1 << 2) #Respuesta es 4

# da 4 por lo siguiente: primero que todo esto (<<) se llama bitwise operadores que actuan sobre numeros enteros pero usando representación 
#binaria el primer numero es el numero que se desplazara y el segundo es el numero de posiciones que se desplazará en este caso se desplaza
# hacia la izquiera entonces el 1 -> 100 y en binario { 0 = 0, 1 = 1, 2 = 10, 3 = 11, 4 = 100} entonces la respuesta es cuatro

# 25. Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
#print(2 + '2')
#No arroja el mismo resultado por que depende del tipo de dato
print(2 + int('2'))
print(str(2) + '2')

# 26.Realizar una operación válida entre valores de tipo entero y string
print(2 + int('2'))
var3 = 'texto '
var4 = 4
print(var3 * var4)