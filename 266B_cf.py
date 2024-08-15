def dom_girls():
    n,t= map(int,input().split())
    l1=list(input())
    for _ in range(t):
        i=0
        while i < len(l1)-1:
            if l1[i]=="B" and l1[i+1]=="G":
                l1[i],l1[i+1]=l1[i+1],l1[i]
                i+=1
            i+=1
    print("".join(l1))

dom_girls()
