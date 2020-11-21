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

def comparar_clusters(clusters_a, clusters_b):
    len_cluster = len(clusters_a)
    for i in range(len_cluster):
        grupo_a = clusters_a[i].mostrar_cluster()
        grupo_b = clusters_b[i].mostrar_cluster()
        #print(grupo_b, grupo_a)
        if grupo_a != grupo_b:
            return True
    return False

def copiar_clusters(lista_de_clusters):
    copia = []
    for cluster in lista_de_clusters:
        copia.append(cluster.copiar())
    
    return copia

def vaciar_clusters(clusters):
    for cluster in clusters:
        cluster.vaciar()
    

def agrupamiento_kmeans(puntos, rango, numero_de_clusters):
    clusters = generar_clusters(numero_de_clusters, rango)
    vectores = generar_data(puntos, rango)
    metricas = generar_metricas(clusters, vectores)
    copia = copiar_clusters(clusters)
    agrupar(clusters, metricas, vectores)
    
    contador = 0
    while comparar_clusters(copia, clusters): 
        metricas = generar_metricas(clusters, vectores)
        copia = copiar_clusters(clusters)
        vaciar_clusters(clusters)
        agrupar(clusters, metricas, vectores)
        contador += 1
        
    print(clusters[0].mostrar_cluster(), clusters[1].mostrar_cluster(), clusters[2].mostrar_cluster())
    print(contador)
    #print(comparar_clusters(copia, clusters))
    #print(metricas)
    
            

if __name__ == '__main__':
    puntos = 30
    rango = 2000

    agrupamiento_kmeans(puntos, rango, 3)