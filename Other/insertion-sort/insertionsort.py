"""
Sortowanie przez wstawianie (insertionsort) - algorytm przypomina sposób sortowania kart w ręce.
Dzielimy tablicę na część posortowaną i nieposortowaną. Kolejne elementy z nieposortowanej części wstawiamy
w odpowiednie miejsce w części posortowanej.

Zł. czasowa: O(n^2), O(n) dla prawie posortowanych danych, zł. pamięciowa: O(1), stabilność: TAK
"""

def insertion_sort(T):
    n=len(T)
    for i in range(1,n):
        # wstawienie elementu w odpowiednie miejsce
        key = T[i] # ten element zostanie wstawiony w odpowiednie miejsce
        j=i-1

        # przesuwanie elementów większych od key
        while j>=0 and T[j]>key:
            T[j+1]=T[j] #przesuwanie elementów
            j-=1
        T[j+1]=key
    return T


T=[29,10,14,37,13]
print(insertion_sort(T))

