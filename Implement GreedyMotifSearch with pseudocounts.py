def symToNum(sym):
	if sym == "A":
		return 0
	if sym == "C":
		return 1
	if sym == "G":
		return 2
	if sym == "T":
		return 3


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
	max = 0
	probableKm = text[0:k]
	for i in range(0,len(text) - k +1):
		prob = 1
		pattern = text[i:i+k]
		for j in range(k):
			l = symToNum(pattern[j])
			prob *= profile[l][j]
		if prob > max:
			max = prob
			probableKm = pattern
	return probableKm

def matrixProfileF(motifs):
	k = len(motifs[0])
	matrix = [[1 for i in range(k)] for j in range(4)]
	for x in motifs:
		for i in range(len(x)):
			j = symToNum(x[i])
			matrix[j][i] += 1
	for x in matrix:
		for y in x:
			y = y/len(motifs)
	return matrix

def agreee(profile):
	str = ""
	for i in range(len(profile[0])):
		max = 0
		loc = 0
		for j in range(4):
			if profile[j][i] > max:
				loc = j
				max = profile[j][i]
		str+=numToSym(loc)
	return str

def count(motifs):
	profile = matrixProfileF(motifs)
	agr = agreee(profile)
	score = 0
	for x in motifs:
		for i in range(len(x)):
			if agr[i] != x[i]:
				score += 1
	return score

def greedyMotifSearch(dna, k, t):
	greedMot = []
	for x in dna:
		greedMot.append(x[0:k])
	for i in range(len(dna[0])-k+1):
		mot = []
		mot.append(dna[0][i:i+k])
		for j in range(1,t):
			matrix = matrixProfileF(mot)
			mot.append(profileMostProbableKmer(dna[j], k, matrix))
		if count(mot) < count(greedMot):
			greedMot = mot
	return greedMot

k, t = map(int, input().split(" "))
DNA = []
for i in range(t):
    DNA.append(str(input()))
a = greedyMotifSearch(DNA, k, t)
for x in a:
	print(x)