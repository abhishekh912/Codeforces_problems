def cheap():
    n,m,a,b=map(int,input().split())
    sp=int(n/m)
    an=n%m
    final=sp*b+an*a
    f2=a*n
    f3=(sp+1)*b
    print(int(min(final,f2,f3)))
cheap()