def marathon():
    n=int(input())
    l1=[]
    l2=[]
    for i in range(n):
        l1=list(map(int,input().split()))
        a=l1[0]
        l1.sort(reverse=True)
        ind=l1.index(a)
        l2.append(ind)
    for y in l2:
        print(y)
marathon()
        