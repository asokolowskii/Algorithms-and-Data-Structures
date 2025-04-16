"""
bardzo prosty algorytm sortowania bąbelkowego,
jest to algorytm o złożności O(n^2),
w najlepszym wypadku posiada złożoność O(1)
(kiedy lista jest już posortowana)
"""
def bubble_sort(T):
    n=len(T)-1
    no_swaps = True
    for i in range(n):
        for j in range(n-i):
            if T[j]>T[j+1]:
                T[j],T[j+1]=T[j+1],T[j]
                no_swaps = False
        if no_swaps:
            return T
    return T

T=[32,7,4,15,17,21,33,56,74,2]
print(bubble_sort(T))