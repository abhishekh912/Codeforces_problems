def passornot():
    n=int(input())
    if not 1<=n<=100:
        exit()
    
    x_levels=[int(num) for num in input().split()]
    for x in x_levels:
        if not 0<=x<=n:
            exit()
    y_levels=[int(num) for num in input().split()]
    for y in y_levels:
        if not 0<=y<=n:
            exit()
    merge_list=list(set(x_levels+y_levels))
    total_levels=list(range(1,n+1))
    if merge_list== total_levels:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")

passornot()

