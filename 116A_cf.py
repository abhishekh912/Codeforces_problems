n=int(input())
l1=[]
for i in range(n):
    cap=tuple(map(int,input().split()))
    l1.append(cap)
t=l1[0][1]
max=l1[0][1]
for _ in range(n-1):
    t=t-l1[1][0]
    l1.pop(0)
    t=t+l1[0][1]
    if max<t:
        max=t
print(max)
