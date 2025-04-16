from collections import deque

def bfs(G,s):
    visited = [False]*len(G) #inicjalizacja tablicy odwiedzin
    distance = [None]*len(G) #tablica przechowująca odległości od s
    queue = deque([s]) #kolejka do przechowywania wierzchołków do odwiedzenia
    visited[s]=True #oznaczam s jako odwiedzony
    distance[s]=0 #odl od s do s wynosi 0

    while queue:
        u = queue.popleft() #pobieramy pierwszy wierzchołek z kolejki
        for v in G[u]: #iterujemy po sąsiadach u
            if not visited[v]:
                visited[v]=True
                distance[v]=distance[u]+1 #odl to odl rodzica +1
                queue.append(v) #dodajemy v do kolejki

    return visited, distance