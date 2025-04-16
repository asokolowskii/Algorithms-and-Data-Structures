"""Sortowanie szybkie - QuickSort - to algorytm "dziel i zwyciężaj".
Działa poprzez wybór elementu zwany pivotem i podzielenie
tablicy na dwie części: elementy mniejsze i większe od pivota.

Czas: O(nlogn) - średnio, O(n^2)-najgorzej
Pamięć: O(logn)
Stabilność: NIE
"""

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i += 1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

    return A

T=[3,7,4,14,22,3,1,22,11,23,46,7,12,2]
print(quicksort(T,0,len(T)-1))




