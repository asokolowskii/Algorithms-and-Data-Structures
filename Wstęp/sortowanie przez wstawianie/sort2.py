"""
Sortowanie przez wstawianie (ang. Insertion Sort)
to jeden z najprostszych algorytmów sortowania,
działający podobnie do sortowania kart w ręce –
elementy są wstawiane jeden po drugim we właściwe
miejsce w już posortowanej części tablicy.

- Złożoność czasowa:
Najlepszy przypadek (tablica już posortowana): O(n)
Średni przypadek: O(n²)
Najgorszy przypadek (tablica posortowana odwrotnie): O(n²)

- Złożoność pamięciowa:
Pamięć dodatkowa: O(1) (sortowanie in-place)
"""

def insertion_sort(T):
    n=len(T)
    for i in range(1, len(T)):
        value=T[i]
        while i>0 and T[i-1]>value:
            T[i]=T[i-1]
            i=i-1
        T[i]=value
    return T

