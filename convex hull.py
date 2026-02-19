"""

Qué hace este programa:
- Lee puntos (x,y) desde un CSV
- Grafica los puntos
- Calcula el Convex Hull (envolvente convexa)
- Dibuja el polígono resultante

Que hacer:
- Completar las funciones marcadas con TODO
- Probar con diferentes conjuntos de puntos

Requisitos:
- Python 3.x
- matplotlib

Instalación (si hace falta):
pip install matplotlib
"""

import csv
from typing import List, Tuple
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox

Point = Tuple[float, float]

def cargar_csv():
    archivo = filedialog.askopenfilename(filetypes=[("CSV", "*.csv"), ("Todos", "*.*")])
    if not archivo:
        return
    puntos = []
    try:
        with open(archivo, newline='') as f:
            lector = csv.reader(f)
            for fila in lector:
                if len(fila) >= 2:
                    x = float(fila[0])
                    y = float(fila[1])
                    puntos.append((x,y))
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el CSV: {e}")
        return

    if len(puntos) < 2:
        messagebox.showerror("Error", "El CSV debe contener al menos 2 puntos.")
        return

 
    hull = convex_hull(puntos)
    dibujar(puntos, hull)

def punto_mas_izquierdo(puntos: List[Point]) -> int:
    """
    Regresa el índice del punto más a la izquierda.
    En empate de x, escoger el de menor y (para hacerlo determinista).
    """
    idx = 0
    for i in range(1, len(puntos)):
        if puntos[i][0] < puntos[idx][0] or (puntos[i][0] == puntos[idx][0] and puntos[i][1] < puntos[idx][1]):
            idx = i
    return idx


def orientacion(a: Point, b: Point, c: Point) -> float:
    """
    Todo:
    Regresa el valor del producto cruz (cross product).

    Pista :
    cross = (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)

    Interpretación:
    - cross > 0  : giro antihorario (CCW)
    - cross < 0  : giro horario (CW)
    - cross == 0 : colineales
    """
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def distancia2(a: Point, b: Point) -> float:
    """Distancia al cuadrado (evita usar sqrt, no hace falta para comparar)."""
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy


def convex_hull(puntos: List[Point]) -> List[Point]:
    """
    Todo:

    Idea general:
    1) Empieza en el punto más a la izquierda.
    2) En cada paso, elige el siguiente punto q tal que para cualquier otro punto r,
       el giro desde p hacia q sea el “más externo”.
    3) Repite hasta regresar al punto inicial.

    Nota:
    - Maneja colineales: si varios puntos quedan en la misma línea,
      quédate con el más lejano para que la envolvente quede “por fuera”.
    """
    if len(puntos) < 3:
        return puntos[:]  # no hay polígono

    hull: List[Point] = []
    start_idx = punto_mas_izquierdo(puntos)
    p_idx = start_idx

    while True:
        hull.append(puntos[p_idx])
        q_idx = (p_idx + 1) % len(puntos)

        for r_idx in range(len(puntos)):
            if r_idx == p_idx:
                continue

            # Todo:
            # 1) Calcula o = orientacion(p, q, r)
            # 2) Si r es “más externo” que q, entonces q = r
            # 3) Si son colineales, elige el más lejano a p
            #
            # Sugerencia de convención:
            # - Si tu orientacion devuelve >0 para CCW,
            #   normalmente querrás elegir el punto con giro CCW “más externo”.
            # Ajusta la condición según tu convención.

            # 1) Calcula o = orientacion(p, q, r)
            o = orientacion(puntos[p_idx], puntos[q_idx], puntos[r_idx])
            
            # 2) Si r es “más externo” (giro CCW) que q, entonces q = r
            if o > 0:
                q_idx = r_idx
            # 3) Si son colineales, elige el más lejano a p
            elif o == 0:
                if distancia2(puntos[p_idx], puntos[r_idx]) > distancia2(puntos[p_idx], puntos[q_idx]):
                    q_idx = r_idx
                    
        p_idx = q_idx
        if p_idx == start_idx:
            break

    return hull

def dibujar(puntos: List[Point], hull: List[Point], titulo: str = "Convex Hull"):
    """Dibuja puntos y el polígono del hull."""
    xs = [p[0] for p in puntos]
    ys = [p[1] for p in puntos]

    plt.figure()
    plt.scatter(xs, ys)

    if len(hull) >= 2:
        hx = [p[0] for p in hull] + [hull[0][0]]
        hy = [p[1] for p in hull] + [hull[0][1]]
        plt.plot(hx, hy)

    plt.title(titulo)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.show()


ventana = tk.Tk()
ventana.title("Hull")
ventana.geometry("460x520")


tk.Button(ventana, text="Cargar CSV", command=cargar_csv).pack(pady=4)

etiqueta_resultado = tk.Label(ventana, text="", fg="blue", justify='left')
etiqueta_resultado.pack(pady=12)

ventana.mainloop()
