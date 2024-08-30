def twins():
    n=int(input())
    result=[]
    l_coins=list(map(int,input().split()))
    s_coins=sorted(l_coins,reverse=True)
    n = len(l_coins)
    lst=sorted(l_coins,reverse=True)
    
    for i in range(1, n+1):
        sum_first_n = sum(lst[:i])
        sum_remaining = sum(lst[i:])
        if sum_first_n>sum_remaining:
            result.append((sum_first_n, sum_remaining,i))
    print(result[0][2])
 
twins()