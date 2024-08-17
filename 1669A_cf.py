def rating():
    t=int(input())
    l1=[]
    for i in range(t):
        inp=int(input())
        if inp>=1900:
            l1.append("Division 1")
        elif inp>=1600 and inp<=1899:
            l1.append("Division 2")
        elif inp>=1400 and inp<=1599:
            l1.append("Division 3")
        elif inp<=1399:
            l1.append("Division 4")
    
    for x in l1:
        print(x)
        
        
rating()