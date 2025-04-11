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