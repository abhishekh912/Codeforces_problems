def equality():
    n=int(input())
    l1=list(map(int,input().split()))
    sum=0
    maxi=max(l1)
    for i in l1:
        sum=sum+(maxi-i)
    print(sum)
equality()
