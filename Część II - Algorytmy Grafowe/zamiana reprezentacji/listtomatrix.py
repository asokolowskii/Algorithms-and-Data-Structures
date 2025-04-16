#Zamiana reprezentacji

#Lista sąsiedztwa -> Macierz sąsiedztwa
def list_to_matrix(T_list):
    n=len(T_list) #liczba wierzchołków
    matrix = [[0]*n for _ in range(n)] #inicjalizacja macierzy
    for u in range(n):
        for v in T_list[u]:
            matrix[u][v]=1 #zaznaczenie istn. krawędzi u->v
    return matrix

#Macierz sąsiedztwa -> Lista sąsiedztwa
def matrix_to_list(T_matrix):
    n=len(T_matrix) #liczba wierzchołków
    T_list = [[] for _ in range(n)] #inicjalizacja pustej listy sąsiedztwa
    for u in range(n):
        for v in range(n):
            if T_matrix[u][v]!=0:
                T_list[u].append(v)
    return T_list

G=[[1],[2],[3,4],[2,4,5],[2,3],[3]]
print(list_to_matrix(G))

M = [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0]]
print(matrix_to_list(M))




















