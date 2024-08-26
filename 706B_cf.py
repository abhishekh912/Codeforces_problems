def drinks():
    shops_num=int(input())
    prices=list(map(int,input().split()))
    days=int(input())
    funds=[]
    result=[]
    m=0
    for _ in range(days):
        funds.append(int(input()))
    
    for x in funds:
        m=0
        for y in prices:
            if x >=y:
                m+=1
        result.append(m)
    for n in result:
        print(n)
    
drinks()