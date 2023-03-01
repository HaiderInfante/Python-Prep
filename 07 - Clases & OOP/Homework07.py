# 1. Crear la clase vehículo que contenga los atributos:
# Color
# Si es moto, auto, camioneta ó camión
# Cilindrada del motor
class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada

# 2. A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:
# Acelerar
# Frenar
# Doblar
class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0

    def acelerar(self,vel):
        self.velocidad  += vel
        return self.velocidad
    def frenar(self, vel):
        self.velocidad  -= vel
        return self.velocidad
    def doblar(self, grados):
        self.direccion += grados
        return self.direccion

# 3. Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado
v1 = Vehiculo('verde', 'moto', 150)
v2 = Vehiculo('rojo', 'auto', 1600)
v3 = Vehiculo('negro', 'camioneta', 2500)

print(v1.acelerar(40))
print(v2.frenar(50))
print(v3.doblar(60))

# 4. Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada
class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0

    def acelerar(self,vel):
        self.velocidad  += vel
    def frenar(self, vel):
        self.velocidad  -= vel
    def doblar(self, grados):
        self.direccion += grados
    def estado(self):
        return print(f'El vehiculo se encuentra a una velocidad de {self.velocidad} y su dirección es de {self.direccion}')
    def mostrar_vehiculo(self):
        return print('Soy', self.tipo, 'de color', self.color, 'y mi cilindrada es de', self.cilindrada, 'litros')

v1 = Vehiculo('verde', 'moto', 150)
print(v1.estado())
print(v1.mostrar_vehiculo())

# 5. Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6
# Verificar Primo
# Valor modal
# Conversión grados
# Factorial

class Operations:
    def __init__(self) -> None:
        pass

    def es_primo (self, n):
        primo = True
        for i in range (2, n):
            if (n % i == 0):
                primo = False
                break
        return primo

    def valor_modal(self, lista):
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

    def conversion_grados(self, valor, origen, destino):
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

    def factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        return numero
    
# 6. Probar las funciones incorporadas en la clase del punto 5
operations = Operations()

print(operations.es_primo(7))
print(operations.valor_modal([1,1,5,6,8,10,22,5,6,4,11,9,5]))
print(operations.conversion_grados(3, 'celsius', 'farenheit'))
print(operations.factorial(5))

# 7. Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas
class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def verifica_primo(self):
        for i in self.lista:
            if (self.__verifica_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversion_grados(i, origen, destino),'grados',destino)
    
    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))

    def __verifica_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo

    def valor_modal(self, menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
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

    def __conversion_grados(self, valor, origen, destino):
        valor_destino = None
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

    def __factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero

# 8. Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones
