"""
Sortowanie pozycyjne - RadixSort - sortuje elementy według kolejnych cyfr od najmniej znaczącej
do najbardziej znaczacej, stosując stabilne sortowanie pomocnicze, np. CountingSort
"""

def counting_sort_digit(A,exp):
    n=len(A)
    B=[None]*n
    C= [0]*10

    for x in A:
        digit = (x//exp)%10
        C[digit]+=1

    for i in range(1,10):
        C[i]+=C[i-1]

    for i in range(n-1,-1,-1):
        digit= (A[i]//exp)%10
        B[C[digit]-1] = A[i]
        C[digit]-=1

    for i in range(n):
        A[i]=B[i]

def radix_sort(A):
    if not A:
        return

    max_val=max(A)
    exp=1 #zaczynamy od jedności

    while max_val //exp > 0:
        counting_sort_digit(A,exp)
        exp*=10




