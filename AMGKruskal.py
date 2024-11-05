# Algoritmo de Kruskal con Union-Find
def UnionFind():
    def find(padres, nodo):
        if padres[nodo] != nodo:
            padres[nodo] = find(padres, padres[nodo])
        return padres[nodo]

    def union(padres, rank, nodo1, nodo2):
        padre1, padre2 = find(padres, nodo1), find(padres, nodo2)
        if padre1 != padre2:
            if rank[padre1] > rank[padre2]:
                padres[padre2] = padre1
            else:
                padres[padre1] = padre2
                if rank[padre1] == rank[padre2]:
                    rank[padre2] += 1

    return find, union

def kruskal(grafo, nodos):
    grafo.sort(key=lambda x: x[2])
    find, union = UnionFind()
    padres = {nodo: nodo for nodo in range(1, nodos + 1)}
    rank = {nodo: 0 for nodo in range(1, nodos + 1)}
    arbol = []
    for nodo1, nodo2, peso in grafo:
        if find(padres, nodo1) != find(padres, nodo2):
            arbol.append((nodo1, nodo2, peso))
            union(padres, rank, nodo1, nodo2)
    return arbol

# Imprimir el AMG
def imprimirAMG(grafo):
    print("Arbol Generador Minimo:")
    for nodo1, nodo2, peso in grafo:
        print(f"{nodo1} - {nodo2}: {peso}")

# Crear un grafo no dirigido ingresado por el usuario
grafo = []
while True:
    try:
        nodos = int(input("Ingrese el número de nodos: "))
        if nodos <= 0:
            raise ValueError("El número de nodos debe ser un entero positivo.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        aristas = input("Ingrese las aristas en formato de una lista separada por comas donde cada separación contenga (nodo1 nodo2 peso) separado por espacios: ")
        aristas = aristas.split(",")
        for arista in aristas:
            nodo1, nodo2, peso = arista.split()
            nodo1, nodo2, peso = int(nodo1), int(nodo2), int(peso)
            if nodo1 > 0 and nodo1 <= nodos and nodo2 > 0 and nodo2 <= nodos:
                grafo.append((nodo1, nodo2, peso))
            else:
                print(f"Arista no válida en el grafo: {arista}")
        break
    except ValueError as e:
        print(e)

print("Grafo Creado:")
print(grafo)

# Calcular el AMG
arbol = kruskal(grafo, nodos)
imprimirAMG(arbol)
