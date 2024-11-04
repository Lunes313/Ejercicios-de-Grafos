import heapq

def dijkstra(grafo, inicio):
    # Inicializamos en infinito la distancia a cada nodo menos el incio
    distancia = {nodo: float('inf') for nodo in grafo}
    distancia[inicio] = 0
    # Cola de prioridad
    cola = [(0, inicio)]
    procesados = {}

    while cola:
        # Se extrae el nodo con menor distancia
        distanciaN, nodo = heapq.heappop(cola)

        # Si el nodo ya fue procesado, se ignora
        if nodo in procesados:
            continue

        # Marcar el nodo como procesado
        procesados[nodo] = distanciaN

        # Recorrer los vecinos del nodo actual
        for vecino, peso in grafo[nodo]:
            distancia_total = distanciaN + peso
            if distancia_total < distancia[vecino]:
                distancia[vecino] = distancia_total
                heapq.heappush(cola, (distancia_total, vecino))

    return distancia

# Crear el grafo ingresado por el usuario con manejo de errores
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
        aristas = input("Ingrese las aristas en formato de una lista separada por comas donde cada separación contenga (nodo1 nodo2 peso) separado por espacios: ")
        aristas = aristas.split(",")
        for arista in aristas:
            nodo1, nodo2, peso = arista.split()
            nodo1, nodo2, peso = int(nodo1), int(nodo2), int(peso)
            if nodo1 > 0 and nodo1 <= nodos and nodo2 > 0 and nodo2 <= nodos:
                grafo[nodo1].append((nodo2, peso))
                if nodo1 != nodo2:
                    grafo[nodo2].append((nodo1, peso))
            else:
                print(f"Arista no válida en el grafo: {arista}")
        break
    except ValueError as e:
        print(e)

print("Grafo")
for nodo, vecinos in grafo.items():
    print(f"{nodo}: {vecinos}")

# Calcular el camino más corto
while True:
    try:
        inicio = int(input("Ingrese el nodo de inicio: "))
        if inicio > 0 and inicio <= nodos:
            break
    except ValueError:
        print("Nodo de inicio no válido.")


distancias = dijkstra(grafo, inicio)
print("Distancias más cortas desde el nodo de inicio:")
for nodo, distancia in distancias.items():
    print(f"{nodo}: {distancia}")
