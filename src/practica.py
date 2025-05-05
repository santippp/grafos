def mostrar_saludo():
    print("hola que tal")

def lee_grafo(grafo):
    cant_vert = int(grafo[0])
    vertices = grafo[1 : 1 + cant_vert]

    aristas = []

    for arista_str in grafo[1 + cant_vert:]:
        nodo1, nodo2 = arista_str.split()
        aristas.append((nodo1, nodo2))

    return (vertices, aristas)

def lee_grafo_archivo(file):
    grafo = []
    with open(file, 'r', encoding='utf-8') as file:
        for linea in file:
            grafo.append(linea.strip())

    cant_vert = int(grafo[0])
    vertices = grafo[1 : 1 + cant_vert]

    aristas = []

    for arista_str in grafo[1 + cant_vert:]:
        nodo1, nodo2 = arista_str.split()
        aristas.append((nodo1, nodo2))

    return (vertices, aristas)

def cuenta_grado(grafo_lista) :
    salida = {}
    vertices, aristas = grafo_lista

    # Inicializar el grado de cada vértice a 0
    for vertice in vertices:
        salida[vertice] = 0

    # Contar las aristas incidentes en cada vértice
    for arista in aristas:
        u, v = arista  # Desempaquetar los vértices de la arista
        if u in salida:
            salida[u] += 1
        if v in salida:
            salida[v] += 1

    print(f"lista: {salida}")

def vertice_aislado(grafo_lista):
    salida = {}
    vertices, aristas = grafo_lista

    # Inicializar el grado de cada vértice a 0
    for vertice in vertices:
        salida[vertice] = 0

    # Contar las aristas incidentes en cada vértice
    for arista in aristas:
        u, v = arista  # Desempaquetar los vértices de la arista
        if u in salida:
            salida[u] += 1
        if v in salida:
            salida[v] += 1
            
    verticescero = []
    i=0
    for vertice in vertices:
        if salida[vertice] == 0:
            verticescero[i] = vertice
            i+=1
    print(f"{verticescero}")

def componentes_conexas(grafo_lista):
    nodos, aristas = grafo_lista
    # Paso 1: Crear un diccionario de adyacencia
    adyacencias = {nodo: [] for nodo in nodos}
    for (nodo1, nodo2) in aristas:
        adyacencias[nodo1].append(nodo2)
        adyacencias[nodo2].append(nodo1)  # Grafo no dirigido

    # Paso 2: Función DFS para explorar los nodos
    def dfs(nodo, visitado, componente):
        visitado.add(nodo)
        componente.append(nodo)
        for vecino in adyacencias[nodo]:
            if vecino not in visitado:
                dfs(vecino, visitado, componente)
    
    # Paso 3: Encontrar las componentes conexas
    visitado = set()
    componentes = []
    
    for nodo in nodos:
        if nodo not in visitado:
            componente = []
            dfs(nodo, visitado, componente)
            componentes.append(componente)
    
    return componentes