n=int(input())
l1=[4,7,47,74,44,444,447,474,477,777,774,744]
flag=False
for i in l1:
    if n%i==0:
        flag=True
    
if flag:
    print("YES")
else:
    print("NO")
