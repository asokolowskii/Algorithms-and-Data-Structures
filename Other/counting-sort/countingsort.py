"""
Sortowanie przez zliczanie (CountingSort) - działa poprzez zliczenie liczby wystąpień każdego elementu,
zakładając, że wartości elementów należą do ograniczonego zakresu liczb całkowitych.

Czas O(n+k), pamięć: O(k), stabilność: TAK
"""

def counting_sort(A,k):
    n=len(A)
    C=[0]*k
    B=[0]*n

    for i in range(n):
        C[A[i]]+=1

    for i in range(1,k):
        C[i]=C[i-1]+C[i]

    for i in range(n-1,-1,-1):
        C[A[i]]-=1
        B[C[A[i]]]=A[i]

    for i in range(n):
        A[i]=B[i]

A = [4, 2, 2, 3, 3, 1]


