def passornot():
    n=int(input())
    if not 1<=n<=100:
        exit()
    
    x_levels=list(map(int,input().split()))
    for x in x_levels:
        if not 0<=x<=n:
            exit()
    player1=x_levels[1:]
    y_levels=list(map(int,input().split()))
    for y in y_levels:
        if not 0<=y<=n:
            exit()
    player2=y_levels[1:]
    merge_list=list(set(player1+player2))
    total_levels=list(range(1,n+1))

    if merge_list== total_levels:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")

passornot()

