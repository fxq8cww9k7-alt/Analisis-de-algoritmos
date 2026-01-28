#Comparador de metodos de ordenamiento
#En este programa se comparan metodos de ordenamiento, midiendo sus tiempos de ejecucion, realizando un analisis Big-O y graficando los resultados obtenidos.
#En caso de requerir mas implementaciones de metodos de ordenamiento, se pueden agregar nuevas funciones siguiendo la estructura de las ya existentes. Solamente cuidadndo las funciones de medicion de tiempo, comparacion y graficacion para incluir los nuevos metodos.
#Este programa utiliza la libreria bigO para el analisis Big-O, la cual debe estar instalada en el entorno de Python. Se puede instalar utilizando pip install bigO. A su vez utiliza matplotlib para la graficacion, la cual puede ser instalada con pip install matplotlib.

from bigO import BigO
from bigO import algorithm
lib = BigO()
import time 
import matplotlib.pyplot as plt


def bubblesort(lista):
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    n = 0 # Establecemos un contador del largo del vector
    
    for _ in lista:
        n += 1 #Contamos la cantidad de caracteres dentro del vector
    
    for i in range(n-1): 
    # Le damos un rango n para que complete el proceso. 
        for j in range(0, n-i-1): 
            # Revisa la matriz de 0 hasta n-i-1
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
            # Se intercambian si el elemento encontrado es mayor 
            # Luego pasa al siguiente
    return lista


def selectionsort(lista): 
    largo = 0
    
    for _ in lista:
        largo += 1 # Obtenemos el largo del vector
        
    for i in range(largo): 
      
        # Encontrar el minimo elemento de los restantes sin ordenar
        minimo = i 
        for j in range(i+1, largo): 
            if lista[minimo] > lista[j]: 
                minimo = j 
                
        # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
        lista[i], lista[minimo] = lista[minimo], lista[i]
        # Repetimos el proceso hasta terminar


def insertionsort(lista): 
    
    largo = 0 # Establecemos un contador del largo
     
    for i in lista:
        largo += 1 # Obtenemos el largo del vector
    
    # Recorremos la lista de 1 hasta el largo del vector
    for i in range(1, largo): 
    
        elemento = lista[i] 
  
        # Movemos los elementos de vectorins[0...i-1], que son mayores que el elemento
        # a una posición adelante de su posición actual
        j = i-1
        while j >= 0 and elemento < lista[j] : 
                lista[j+1] = lista[j] 
                j -= 1
        lista[j+1] = elemento 


def shellsort(lista):
      
    largo = 0
    
    for i in lista:
        largo += 1
    
    distancia = largo // 2
    
     # Creamos un bucle según las distancias
    while distancia > 0:
        # Utilizamos el Insertionsort
        for i in range(distancia, largo):
            val = lista[i]
            j = i
            while j >= distancia and lista[j - distancia] > val:
                lista[j] = lista[j - distancia]
                j -= distancia
            lista[j] = val
        distancia //= 2 # Acotamos la distancia nuevamente y continua el ciclo


def quicksort(lista, start = 0, end = None):
    if end is None:
        end = len(lista) - 1
    def quick(lista, start = 0, end = None):
        if end is None:
            end = len(lista) - 1
        
        if start >= end:
            return

        def particion(lista, start = 0, end = None):
            if end is None:
                end = len(lista) - 1
            pivot = lista[start]
            menor = start + 1
            mayor = end

            while True:
                # Si el valor actual es mayor que el pivot
                # está en el lugar correcto (lado derecho del pivot) y podemos 
                # movernos hacia la izquierda, al siguiente elemento.
                # También debemos asegurarnos de no haber superado el puntero bajo, ya que indica 
                # que ya hemos movido todos los elementos a su lado correcto del pivot
                while menor <= mayor and lista[mayor] >= pivot:
                    mayor = mayor - 1

                # Proceso opuesto al anterior            
                while menor <= mayor and lista[menor] <= pivot:
                    menor = menor + 1

                # Encontramos un valor sea mayor o menor y que este fuera del arreglo
                # ó menor es más grande que mayor, en cuyo caso salimos del ciclo
                if menor <= mayor:
                    lista[menor], lista[mayor] = lista[mayor], lista[menor]
                    # Continua el bucle
                else:
                    # Salimos del bucle
                    break

            lista[start], lista[mayor] = lista[mayor], lista[start]
            
            return mayor
        
        p = particion(lista, start, end)
        quick(lista, start, p-1)
        quick(lista, p+1, end)
        
        quick(lista)


def medir_tiempo(algoritmo, lista):
    copia = lista.copy()  
    inicio = time.perf_counter()
    algoritmo(copia)
    fin = time.perf_counter()
    return fin - inicio


def lista_peor_caso():#Funcion que genera la lista en peor caso (lista ordenada de mayor a menor)
    return list(range(1000, 49, -50))


def comparacion():#Funcion principal de comparacion de tiempos 

    tamanios = range(1000, 0, -50)

    tiempos = {
        "Bubble Sort": 0,
        "Selection Sort": 0,
        "Insertion Sort": 0,
        "Shell Sort": 0,
        "Quick Sort": 0
    }

    for n in tamanios:
        base = lista_peor_caso()

        inicio = time.perf_counter()
        bubblesort(base.copy())
        tiempos["Bubble Sort"] += time.perf_counter() - inicio

        inicio = time.perf_counter()
        selectionsort(base.copy())
        tiempos["Selection Sort"] += time.perf_counter() - inicio

        inicio = time.perf_counter()
        insertionsort(base.copy())
        tiempos["Insertion Sort"] += time.perf_counter() - inicio

        inicio = time.perf_counter()
        shellsort(base.copy())
        tiempos["Shell Sort"] += time.perf_counter() - inicio

        inicio = time.perf_counter()
        quicksort(base.copy())
        tiempos["Quick Sort"] += time.perf_counter() - inicio

    print("\nAlgoritmo        Tiempo total (s)")
    print("--------------------------------")
    for alg, t in tiempos.items():
        print(f"{alg:<15} {t:.6f}")

    return tiempos


def graficar_tiempos(tiempos):#Funcion encargada de graficar los tiempos obtenidos
    algoritmos = list(tiempos.keys())
    valores = list(tiempos.values())

    plt.figure()
    plt.bar(algoritmos, valores)
    plt.xlabel("Algoritmo")
    plt.ylabel("Tiempo total (s)")
    plt.title("Comparacion de algoritmos de ordenamiento (Peor caso)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


def analisis_big_o():#funcion encargada de realizar el analisis Big-O de los algoritmos
    print("\nAnalisis Big-O (libreria bigO)")
    print("--------------------------------")

    lib.test(bubblesort, "random")
    lib.test(selectionsort, "random")
    lib.test(insertionsort, "random")
    lib.test(shellsort, "random")
    lib.test(quicksort, "random")



if __name__ == "__main__": #Ejecuta las funciones principales
    tiempos=comparacion()
    comparacion()
    analisis_big_o()
    graficar_tiempos(tiempos)