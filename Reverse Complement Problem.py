Text = input()
res = ""
Text = Text[::-1]
for i in range (len(Text)):
    if Text[i] == 'A':
        res += 'T'
    elif Text[i] == 'C':
        res += 'G'
    elif Text[i] == 'G':
        res += 'C'
    elif Text[i] == 'T':
        res += 'A'
print(res)