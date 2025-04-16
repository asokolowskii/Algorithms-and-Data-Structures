"""
-Funkcja DFS przyjmuje graf G w postaci listy sąsiedztwa oraz wierzchołek początkowy s.
-Wewnątrz niej definiowana jest funkcja pomocnicza dfs_visit, która odwiedza wierzchołki rekurencyjnie.
-Tablica visited przechowuje informację, które wierzchołki zostały już odwiedzone.
-Tablica parent zapamiętuje, z którego wierzchołka dotarliśmy do danego wierzchołka — tworząc w ten sposób drzewo DFS.
-Na końcu zwracana jest krotka (visited, parent)
"""

# Funkcja pomocnicza do rekurencyjnego odwiedzania wierzchołków
# G - graf w postaci listy sąsiedztwa
# u - aktualnie odwiedzany wierzchołek
# visited - lista bool wskazująca, które wierzchołki zostały odwiedzone
# parent - lista przechowująca rodziców wierzchołków

def dfs_visit(G,u,visited, parent):
    visited[u]=True # Oznacz u jako odwiedzony
    for v in G[u]: # Iteruj po sąsiadach u
        if not visited[v]: # Jeżeli sąsiad v nie został jeszcze odwiedzony
            parent[v]=u # Zapamiętaj, że u jest rodzicem v
            dfs_visit(G,v,visited, parent) ## Odwiedź v rekurencyjnie

def DFS(G,s):
    visited = [False]*len(G) # Inicjalizacja odwiedzin
    parent = [None]*len(G) # Inicjalizacja listy rodziców
    dfs_visit(G,s,visited,parent) # Rozpoczęcie DFS od s
    return visited, parent




