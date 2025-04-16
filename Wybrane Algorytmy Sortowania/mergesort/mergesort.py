'''sortowanie przez scalanie (mergesort):
-dzielimy tablice na 2 części (divide and conquer)
-sortujemy rekurencyjnie połówki
-mając połówki posortowane lecimy po kolei i łączymy połówki
'''

"""
Merge Sort dzieli tablicę na pół, 
aż każda część będzie miała tylko jeden element. 
Następnie scala te części w taki sposób, aby były posortowane. 
Podczas scalania porównuje się elementy z dwóch części 
i układa w odpowiedniej kolejności. 
Algorytm działa w czasie O(nlog n), co oznacza, 
że jest szybki nawet przy dużych danych.
"""

def mergesort(T,left,right):
    if left<right:
        mid=(left+right)//2
        mergesort(T,left,mid)
        mergesort(T,mid+1,right)

        T_left=T[left:mid+1]
        T_right=T[mid+1:right+1]
        left_ind=right_ind=0
        main_ind=left

        while left_ind<len(T_left) and right_ind<len(T_right):
            if T_left[left_ind]<=T_right[right_ind]:
                T[main_ind]=T_left[left_ind]
                left_ind+=1
            else:
                T[main_ind]=T_right[right_ind]
                right_ind+=1
            main_ind+=1

        while left_ind<len(T_left):
            T[main_ind]=T_left[left_ind]
            left_ind+=1
            main_ind+=1

        while right_ind < len(T_right):
            T[main_ind] = T_right[right_ind]
            right_ind += 1
            main_ind += 1

    return T

T=[13,7,2,1,55,4,222,11,4,68,0,8,0,4,3]
print(mergesort(T,0,len(T)-1))
