# Practica 1 - Medicion empirica de complejidad
# Analisis de Algoritmos
# Codigo base de ejemplo
# Lenguaje: Python 3

import time #importa libreria "time"
import random #importa libreria "random"

def recorrido_simple(lista): #define una funcion que recibe el parametro lista 
    total = 0 #Crea la variable total y la iguala a 0
    for x in lista: #hace un for que se ejecuta por cada elemento en lista 
        total += x #le suma el valor de x a la variable total 
    return total #la funcion devuelve la variable total 

def doble_ciclo(lista): #Define una funcion que recibe de parametro lista 
    contador = 0 #se crea una variable contador que se iguala a 0
    for i in range(len(lista)): #Un for que se ejecuta por el valor que devuelve len, que es la longitud de elementos de lista 
        for j in range(len(lista)): #Un for dentro de otro for que se ejecuta por el valor que devuelve len, que es la longitud de elementos de lista
            contador += lista[i] * lista[j] #le suma al contador el valor de lista del numero i multuiplicado por el numero j que esta en la lista que vienen del for 
    return contador #la funcion devuelve la variable contador 

def experimento(): #define una funcion sin parametro de entrada
    tamanios = [1000, 5000, 10000, 20000] #crea una lista con diversos valores
    print("Tamano | Recorrido simple (s) | Doble ciclo (s)")#imprime 
    print("----------------------------------------------")#imprime

    for n in tamanios: #crea un for que entradara por cada parametro en tamanios o sea 4 veces
        datos = [random.randint(1, 100) for _ in range(n)] #crea una varible datos, en la que toma un numero random en un rango de 1-100, esto lo hace las veces que es igual al tamaño de n(1000)

        inicio = time.time() #empieza el contador de tiempo 
        recorrido_simple(datos) #convoca a la funcion con el parametro datos 
        t1 = time.time() - inicio #cierra el tiempo dando y lo guarda en la variable t1

        inicio = time.time() #inicia el contador del tiempo 
        doble_ciclo(datos) #convoca a la funcion doble ciclo y manda datos que es el numero de tamanios
        t2 = time.time() - inicio #detiene el contador y lo guarda en t2 

        print(f"{n:6d} | {t1:20.6f} | {t2:15.6f}") #primero formatea la variable "n" como un decimal de 6 caracteres, si son menos se rellena y alinea a la izquierda, luego formatea el t1 por una numero de tipo flotante, luego se define el ancho minimo en 20, y que sera de 6 caracteres, lo mismo para el t2 pero con distintos longitudes

if __name__ == "__main__": #un codigo que sirve para ejecutar solo el bloque de codigo que quieras en este caso la funcion experimento 
    experimento()