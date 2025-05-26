import src.practica as p1

p1.mostrar_saludo()
a = ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
p1.lee_grafo(a)


b = p1.lee_grafo_archivo("hola.txt")

print(f":{b}")

c = (['A','B','C','D'],[('A','B'),('B','C'),('C','B')])

p1.cuenta_grado(c)

p1.vertice_aislado(c)

d = (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
e = p1.componentes_conexas(d)

print(f"conexo: {e}")
