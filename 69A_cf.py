n=int(input())
l1=[]
sum1,sum2,sum3=0,0,0
for _ in range(n):
    x=tuple(map(int,input().split()))
    l1.append(x)
for x in range(n):
    sum1+=l1[x][0]
    sum2+=l1[x][1]
    sum3+=l1[x][2]
if sum1==0 and sum2==0 and sum3==0:
    print("YES")
else:
    print("NO")