str1 = str(input())
str0 = str(input())
i = 0
c = 0
start = 0
while len(str0):
    i = str0.find(str1,start)
    if (i != -1):
        start = i + 1
        c += 1
    else: 
        break
print(c)