def contiene_ciclo(grafo):
    visitados = []
    for nodo in grafo:
        if nodo not in visitados:
            if dfs(grafo, nodo, visitados, -1):
                return True
    return False

def dfs(grafo, nodo, visitados, padre):
    visitados.append(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            if dfs(grafo, vecino, visitados, nodo):
                return True
        elif padre != vecino:
            return True
    return False

# Crear un grafo no dirijido ingresado por el usuario
grafo = {}
while True:
    try:
        nodos = int(input("Ingrese el número de nodos: "))
        if nodos <= 0:
            raise ValueError("El número de nodos debe ser un entero positivo.")
        break
    except ValueError as e:
        print(e)

for i in range(nodos):
    grafo[i + 1] = []

while True:
    try:
        for i in range(nodos):
            aristas = input(f"Ingrese las aristas del nodo {i + 1} separadas por espacio (a1 a2 a3): ")
            aristas = aristas.split()
            for arista in aristas:
                arista = int(arista)
                if arista > 0 and arista <= nodos:
                    if arista not in grafo[i + 1]:
                        grafo[i + 1].append(arista)
                        grafo[arista].append(i + 1) if arista != i + 1 else None
                else:
                    print(f"Arista no válida en el grafo: {arista}")
        break
    except ValueError as e:
        print(e)

print("Grafo Creado:")
for nodo, vecinos in grafo.items():
    print(f"{nodo}: {vecinos}")

print(contiene_ciclo(grafo))
