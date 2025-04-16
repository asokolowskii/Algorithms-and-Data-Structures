from random import randint
"""
wyszukiwanie liniowe ma złożoność O(n),
w najlepszym przypadku jego złożoność wynosi O(1),
używamy kiedy elementy nie są posortowane
"""

def linear_search(T, n):
    for i in T:
        if i==n:
            return True
    return False


T=[randint(1,20) for _ in range(20)]
print(T)
print(linear_search(T,6))

###############################
"""funkcja wbudowana in"""
unsorted_list = [4,32,5,17,88,41,2,31,15]
print(41 in unsorted_list)
