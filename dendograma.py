
class Dendograma:

    def __init__(self):
        self.capas = []
        self.n_capas = 0

    def agregar_capa(self, clusters):
        capa = {
            "No. capa": self.n_capas,
            "No. clusters": len(clusters),
            "Clusters": clusters
        }
        self.capas.append(capa)
        self.n_capas += 1

    def obtener_capa(self, capa):
        return self.capas[capa]

if __name__ == '__main__':
    dend = Dendograma()
    lista = list(range(20))
    doble = [i * 2 for i in lista]
    dend.agregar_capa(doble)
    print(dend.capas)