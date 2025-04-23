def mostrar_saludo():
    print("hola que tal")

def lee_grafo_stdin(grafo):
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

