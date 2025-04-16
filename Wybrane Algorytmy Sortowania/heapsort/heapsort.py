"""Sortowanie kopcowe (HeapSort) - polega na zbudowaniu kopca maksymalnego (max-heap),
a następnie wielokrotnym zdejmowaniu największego elementu i przywracaniu struktury kopca.
Czas: O(nlogn), Pamięć: O(1), Stabilność: NIE
"""

"""Przywracanie własności kopca"""

def heapify(arr, n, i):
    largest = i  # Korzeń
    left = 2 * i + 1  # Lewe dziecko
    right = 2 * i + 2  # Prawe dziecko

    # Sprawdzamy, czy lewe dziecko jest większe niż korzeń
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Sprawdzamy, czy prawe dziecko jest większe niż największy dotychczas
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Jeśli największy nie jest korzeniem, zamieniamy miejscami i kontynuujemy naprawę
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_heap(arr):
    n = len(arr)
    # Budujemy kopiec, zaczynając od ostatniego węzła niebędącego liściem
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heapsort(arr):
    n = len(arr)
    build_heap(arr)

    # Stopniowo wyciągamy elementy z kopca
    for i in range(n - 1, 0, -1):
        # Przenosimy największy element (korzeń) na koniec
        arr[i], arr[0] = arr[0], arr[i]
        # Naprawiamy kopiec na zmniejszonym zbiorze danych
        heapify(arr, i, 0)


# Przykład użycia
arr = [4, 10, 3, 5, 1]
heapsort(arr)
print("Posortowana tablica:", arr)









