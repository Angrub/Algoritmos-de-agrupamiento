from generar_datos import generar_data
from cluster import Cluster
from random import randint, choice

def generar_clusters(numero_de_clusters, rango):
    clusters = []
    for _ in range(numero_de_clusters):
        cluster = Cluster()
        cluster.x = randint(0,rango) * choice([1, -1])
        cluster.y = randint(0,rango) * choice([1, -1])
        clusters.append(cluster)
    
    return clusters

def generar_metricas(clusters, vectores):
    distancias_clusters = []

    for cluster in clusters:

        distancias_cluster = []
        for vector in vectores:
            distancia = cluster.distancia(vector)
            distancias_cluster.append(distancia)
        
        distancias_clusters.append(distancias_cluster)
    
    return distancias_clusters

def agrupar(clusters, metricas, vectores):
    len_metricas = len(metricas)
    metrica_cluster = metricas[0]
    for i in range(len(metrica_cluster)):
        distancia = metrica_cluster[i]
        
        for j in range(len_metricas - 1):
            metrica_otro_cluster = metricas[j + 1]
            #print(distancia, metrica_otro_cluster[i])
            if distancia > metrica_otro_cluster[i]:
                distancia = metrica_otro_cluster[i]

        for k in range(len_metricas):
            metrica_otro_cluster = metricas[k]
            if distancia == metrica_otro_cluster[i]:
                clusters[k].agregar_vector(vectores[i])
        #print(clusters[0].mostrar_cluster(), clusters[1].mostrar_cluster(), clusters[2].mostrar_cluster()) 

def agrupamiento_kmeans(puntos, rango, numero_de_clusters):
    clusters = generar_clusters(numero_de_clusters, rango)
    vectores = generar_data(puntos, rango)
    metricas = generar_metricas(clusters, vectores)
    agrupar(clusters, metricas, vectores)

    print(clusters[0].mostrar_cluster(), clusters[1].mostrar_cluster(), clusters[2].mostrar_cluster()) 
    print(metricas)
    
            

if __name__ == '__main__':
    puntos = 15
    rango = 20

    agrupamiento_kmeans(puntos, rango, 3)