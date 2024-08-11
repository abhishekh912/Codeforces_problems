def chatRoom(string):
    j=0
    main="hello"
    for char in string:
        if char==main[j]:
            j+=1
        if j==len(main):
            return "YES"
    return "NO"

print(chatRoom(str(input())))