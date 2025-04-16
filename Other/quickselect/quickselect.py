"""
Algorytm Quickselect - quickselect to algorytm służący do znajdowania
k-tego najmniejszego elementu w nieposortowanej tablicy.
Bazuje na podejściu "dziel i zwyciężaj" podobny do quicksort, ale rekurencję
wykonuje tylko po jednej stronie tablicy (tej, w której znajduje się szukany element)
"""

def partition(A, p, r):
    x = A[r]            # Wybieramy pivot jako ostatni element w przedziale [p, r]
    i = p - 1           # 'i' to indeks ostatniego elementu <= pivot

    # Przechodzimy przez każdy element od p do r-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1                      # Zwiększamy indeks "strefy mniejszych"
            A[i], A[j] = A[j], A[i]     # Zamieniamy miejscami A[j] i A[i]

    # Umieszczamy pivot za ostatnim elementem ≤ pivot
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1           # Zwracamy nowy indeks pivota — jego właściwe miejsce

def select(A, p, r, k):
    # Jeśli zakres zawiera tylko jeden element, to go zwracamy
    if p == r:
        return A[p]

    # Dzielimy tablicę wokół pivota
    q = partition(A, p, r)

    # Jeśli pivot jest dokładnie na pozycji k, to to jest nasz wynik
    if q == k:
        return A[q]
    # Jeśli k jest mniejsze, szukamy po lewej stronie
    elif k < q:
        return select(A, p, q - 1, k)
    # Jeśli k jest większe, szukamy po prawej stronie
    else:
        return select(A, q + 1, r, k)
