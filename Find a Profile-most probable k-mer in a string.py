def patternToNum(pattern):
	if len(pattern) == 0:
		return 0
	return 4 * patternToNum(pattern[0:-1]) + symToNum(pattern[-1:])

def symToNum(sym):
	if sym == "A":
		return 0
	if sym == "C":
		return 1
	if sym == "G":
		return 2
	if sym == "T":
		return 3

def numToPattern(tmp, k):
	if k == 1:
		return numToSym(tmp)
	return numToPattern(tmp // 4, k-1) + numToSym(tmp % 4)

def numToSym(tmp):
	if tmp == 0:
		return "A"
	if tmp == 1:
		return "C"
	if tmp == 2:
		return "G"
	if tmp == 3:
		return "T"

def profileMostProbableKmer(text, k, profile):
	probableKm = [0] * 4**k
	for i in range(len(text) - k +1):
		prob = 1
		pattern = text[i:i+k]
		for j in range(k):
			l = symToNum(pattern[j])
			prob *= profile[l][j]
		probableKm[patternToNum(pattern)] = prob
	m = max(probableKm)
	for x in range(4**k):
		if probableKm[x] == m:
			return numToPattern(x, k)

text =str(input())
k = int(input())
matrix=[[0] * k for i in range(4)]
temp=[]
for i in range (4):
    temp=list(map(float, input().split()))
    for j in range(k):
        matrix[i][j]=temp[j]
print(profileMostProbableKmer(text, k, matrix))