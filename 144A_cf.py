def commandos():
    n=int(input())
    l1=list(map(int,input().split()))
    maxi=max(l1)
    mini=min(l1)
    max_list=[]
    min_list=[]
    for i in range(len(l1)):
        if maxi==l1[i]:
            maxi_posi=i+1
            max_list.append(maxi_posi)
        if mini==l1[i]:
            mini_posi=i+1
            min_list.append(mini_posi)
    min_height_max_posi=max(min_list)
    max_height_min_posi=min(max_list)
    steps=(max_height_min_posi-1)+(n-min_height_max_posi)
    if max_height_min_posi<min_height_max_posi:
        print(steps)
    else:
        print(steps-1)

commandos()