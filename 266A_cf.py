n=int(input())
j=0
inp1=str(input())
for x in range(len(inp1)-1):
    if (inp1[x]==inp1[x+1]):
        j+=1
print(j)