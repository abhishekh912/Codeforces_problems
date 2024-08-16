def lucky():
    n=int(input())
    l2=[]
    
    for _ in range(n):
        inp=(input())
        sum1,sum2=0,0
        for x in range(3):
            sum1 += int(inp[x])

        for y in range(3,6):
            sum2 += int(inp[y])
        if sum1 == sum2:
            l2.append("yes")
        else:
            l2.append("no")
    for result in l2:
        print(result)
lucky()