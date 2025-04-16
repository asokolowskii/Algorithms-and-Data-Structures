def insertion_sort(T):
    n=len(T)
    for i in range(1,n):
        key=T[i]
        j=i-1

        while j>=0 and T[j]>key:
            T[j+1]=T[j]
            j-=1
        T[j+1]=key

def bucket_sort(T):
    n=len(T)
    if n==0:
        return

    # 1. Tworzymy n kubełków
    buckets = [[] for _ in range(n)]

    # 2. Rozdzielamy elementy do kubełków
    for x in T:
        index = int(x*n)
        buckets[index].append(x)

    # 3. Sortujemy każdy kubełek
    for bucket in buckets:
        insertion_sort(bucket)

    # 4. Sklejamy kubełki z powrotem do T
    i=0
    for bucket in buckets:
        for x in bucket:
            T[i]=x
            i+=1
