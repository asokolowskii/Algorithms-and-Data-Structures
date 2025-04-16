"""
Sortowanie przez wybieranie (SelectionSort) polega na wielokrotnym wybieraniu
najmniejszego (lub największego) elementu z nieposortowanej części tablicy
i umieszczaniu go na początku.

Złożoność czasowa: O(n^2), zł. pamięciowa: O(1), Stabilność: NIE
"""

def selection_sort(T):
    n=len(T)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if T[j]<T[min_idx]:
                min_idx=j

        T[i],T[min_idx]=T[min_idx],T[i]
    return T

T=[29,10,14,37,13]
print(selection_sort(T))