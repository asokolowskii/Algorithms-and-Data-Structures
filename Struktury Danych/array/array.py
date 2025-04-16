"""
przeszukiwanie nieposortowanej tablicy: O(n)
-odwołanie: O(1)
-wstawianie: O(n)
-usuwanie: O(n)
przeszukiwanie posortowanej tablicy: O(logn)
"""

# Tworzenie tablic
import array

arr = array.array('f', (1.0, 1.5, 2.0, 2.5)) # 'f' - typ danych (float)
print(arr)
print(list(arr))
print(arr[1])

# Przesuwanie zer

T = [8,0,3,0,12]
def move_zeros(T): #Złożoność: O(n)
    zero_index=0
    for index, n in enumerate(T): # funkcja enumerate do pobierania indeksu elementu i jego wartości jednocześnie
        if n!=0:
            T[zero_index]=n
            if zero_index != index:
                T[index]=0
            zero_index+=1
    return T

move_zeros(T)
print(T)



####################################
T1 = [4,0,2,7,0,1]
def move_zeros1(T1):
    zero_index=0
    for index, val in enumerate(T1):
        if val!=0:
            T1[zero_index]=val
            if zero_index!=index:
                T1[index]=0
            zero_index+=1
    return T1

move_zeros(T1)
print(T1)

"""
T1 = [4,0,2,7,0,1]
0. zero_index = 0, n=4, T[zero_index=0] = 4
1. zero_index=1, val = 0
2. zero_index=1, n=2, T[zero_index=1] = 2, T[index=2] = 0  -> T=[4,2,0,7,0,1]
3. zero_index=2, n=7, T[zero_index=2] = 7, T[index=3] = 0  -> T=[4,2,7,0,0,1]
4. zero_index=3, n=1, T[zero_index=3] = 1, T[index=5] = 0  -> T=[4,2,7,1,0,0]
"""


# Łączenie dwóch list

movie_list = ["Interstellar", "Incepcja", "Prestiż", "Bezsenność", "Batman: Początek"]
ratings_list = [1, 10, 10, 8, 6]

# W tym celu używamy funkcji wbudowanej zip
merged_list = list(zip(movie_list, ratings_list))
print(merged_list)

# Znajdowanie powtórzeń w listach
# W tym rozwiązaniu wykorzystamy sety, ponieważ porównanie każdego elementu
# ze wszystkimi pozostałymi ma złożonośc O(n^2) - pętle zagnieżdżone
"""Zbiór (set) to struktura danych, która nie może zawierać powtarzających się elementów"""

new_set = set()
new_set.add("Kanye West")
new_set.add("Kanye West") # doda tylko raz dany element
new_set.add("Kendall Jenner")
new_set.add("Justin Bieber")
print(new_set)

def return_dupl(T2):
    dupl = []
    a_set = set()

    for item in T2:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        if l1 == l2:
            dupl.append(item)

    return dupl

T2 = ["Zuzanna Kowalska", "Krzyś Dobrzyński", "Julka Adamczyk", "Zuzanna Kowalska"]
print(return_dupl(T2))

# Znajdowanie części wspólnej dwóch list
this_weeks_winners = [2,43,48,62,64,28,3]
most_common_winners = [1,28,42,70,2,10,62,31,4,14]

def return_inter(list1, list2):
    list3 = [v for v in list1 if v in list2] # użycie in wewnątrz pętli for: O(n^2)
    return list3

print(return_inter(this_weeks_winners, most_common_winners))

"""2sp. -> wykorzystanie funkcji intersection, 
która zwraca elementy występujace w dwóch lub większej liczbie zbiorów"""

def return_inter1(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    inter_list = list(set1.intersection(set2))

    return inter_list

print(return_inter1(this_weeks_winners, most_common_winners))
