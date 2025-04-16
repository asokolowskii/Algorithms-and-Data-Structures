
"""
wyszukiwanie binarne posiada złożonośc O(logn)
dzieli tablicę na coraz to mniejsze połowy,
porównując aktualny środkowy element z obiema
połowami tablicy
używamy wyszukiwania binarnego do
posortowanych wcześniej elementów
"""

def binary_search(T,n):
    first = 0
    last = len(T)-1
    while last>=first:
        mid = (first+last)//2
        if T[mid] == n:
            return True
        else:
            if T[mid] < n:
                first = mid+1
            else:
                last = mid-1
    return False

T = [1, 3, 5, 7, 9, 11, 15, 20]  # Example sorted list
print(binary_search(T, 9))  # Expected output: True


from bisect import bisect_left
####################################
"""funkcja wbudowana bisect_left z biblioteki bisect"""
def binary_search(T, n):
    index = bisect_left(T, n)
    if index < len(T) and T[index]==n:
        return True
    return False

print(binary_search(T, 9))