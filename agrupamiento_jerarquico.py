from generar_datos import generar_data
from cluster import Cluster
from dendograma import Dendograma

def generar_clusters(puntos, rango):
    lista_de_vectores = generar_data(puntos,rango)
    clusters = []

    for vector in lista_de_vectores:
        cluster = Cluster()
        cluster.agregar_vector(vector)
        clusters.append(cluster)

    return clusters

def generar_metricas(clusters):
    distancias = []
    vinculos = {}
    for cluster_a in clusters:
        for cluster_b in clusters:
            if cluster_a != cluster_b:
                distancia = cluster_a.distancia(cluster_b)
                try:
                    clusters_del_vinculo = vinculos[distancia]
                    primer_par_de_clusters = clusters_del_vinculo[0]
                    segundo_cluster = primer_par_de_clusters[1] # Corrobora que no sea el mismo par de clusters    
                    if cluster_a !=  segundo_cluster:           #       los que dieron la misma distacia
                        vinculos[distancia].append((cluster_a, cluster_b))
                except KeyError:
                    vinculos[distancia] = [(cluster_a, cluster_b)]
                distancias.append(distancia)
    
    return distancias, vinculos 

def agrupar(clusters, distancias, vinculos):
    distancia_min = min(distancias)
    clusters_del_vinculo = vinculos[distancia_min]
    nuevos_clusters = clusters[::]

    for par_de_clusters in clusters_del_vinculo:
        cluster_a = par_de_clusters[0]
        cluster_b = par_de_clusters[1]
        nuevo_cluster = cluster_a.sumar_cluster(cluster_b)
        nuevos_clusters.remove(cluster_a)
        nuevos_clusters.remove(cluster_b)
        nuevos_clusters.append(nuevo_cluster)

    return nuevos_clusters

def agrupamiento_jerarquico(puntos, rango):
    clusters = generar_clusters(puntos, rango)  #
    dendograma = Dendograma()                   # Iniciamos el dendograma y agregamos la capa 0
    dendograma.agregar_capa(clusters)           #

    while len(clusters) > 1:
        distancias, vinculos = generar_metricas(clusters)
        clusters = agrupar(clusters, distancias, vinculos)
        dendograma.agregar_capa(clusters)
    
    return dendograma
            

if __name__ == '__main__':
    
    puntos = 10
    rango = 20
    dendograma = agrupamiento_jerarquico(puntos, rango)
    