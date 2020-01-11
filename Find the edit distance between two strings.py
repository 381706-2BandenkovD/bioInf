def editDist(s1, s2):
    s1Len = len(s1)
    s2Len = len(s2)
    eDist = [[0 for j in range(s2Len + 1)] for i in range(s1Len+1)]
    for i in range(1, s1Len + 1): eDist[i][0] = i 
    for j in range(1, s2Len + 1): eDist[0][j] = j
    for i in range(1, s1Len + 1):
        for j in range (1, s2Len + 1):
            if s1[i-1] == s2[j-1]:
                eDist[i][j] = eDist[i-1][j-1]
            else:
                eDist[i][j] = min(eDist[i-1][j] +1, eDist[i][j-1] + 1, eDist[i-1][j-1] + 1)
    return eDist[s1Len][s2Len]

str1 = input()
str2 = input()
print(editDist(str1, str2))