from vector import Vector

class Cluster(Vector):
    
    def __init__(self, vectores=[]):
        super().__init__(0,0)
        self.grupo = vectores[::]
        self.n_vectores = 0
    
    def agregar_vector(self, vector):
        self.grupo.append(vector)
        self.calcular_centro()

    def sumar_cluster(self, cluster):
        suma_de_clusters = self.mostrar_cluster() + cluster.mostrar_cluster()
        nuevo_cluster = Cluster(suma_de_clusters)
        return nuevo_cluster    

    def mostrar_cluster(self):
        return self.grupo

    def calcular_centro(self):
        coord_x = 0
        coord_y = 0
        self.n_vectores = len(self.grupo)
 
        for vector in self.grupo:
            coord_x += vector.x
            coord_y += vector.y

        self.x = round(coord_x / self.n_vectores,4)
        self.y = round(coord_y / self.n_vectores,4)

    def copiar(self):
        return Cluster(self.grupo)

    def vaciar(self):
        self.grupo.clear()

if __name__ == '__main__':
    cluster = Cluster()
    cluster.agregar_vector(Vector(4,10))
    cluster.agregar_vector(Vector(-6,8))
    cluster.agregar_vector(Vector(9,0))
    print(f'x:{cluster.x} y {cluster.y}')
    