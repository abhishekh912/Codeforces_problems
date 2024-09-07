def insomnia():
    inputs=[]
    final_list=[]
    for y in range(5):
        inp=int(input())
        inputs.append(inp)
    for k in range(4):
        final_list.extend(injured(inputs[k],inputs[4]))
        
    length=len(set(final_list))
    print(length)
    
def injured(x,d):
    l1=[i for i in range(x,d+1,x)]
    return l1

insomnia()