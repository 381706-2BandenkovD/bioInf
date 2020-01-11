n = int(input())
peptides = input()
spectrum = [int(number) for number in peptides.split(' ')]
def expand(list):
	peps = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
	newlist = []
	for x in list:
		for z in peps:
			y = x.copy()
			y.append(z)
			newlist.append(y)
	return newlist

def cycSpec(peptide):
	spec = [0]
	for x in range(1,len(peptide)):
		for i in range(len(peptide)):
			if i+x >= len(peptide):
				y = i+x-len(peptide)
				spec.append(sum(peptide[i:])+sum(peptide[:y]))
			else:
				spec.append(sum(peptide[i:i+x]))
	spec.append(sum(peptide))
	spec.sort()
	return spec

def linSpec(peptide):
	spec = [0]
	for x in range(1,len(peptide)):
		for i in range(len(peptide)):
			if i+x <= len(peptide):
				spec.append(sum(peptide[i:i+x]))
	spec.append(sum(peptide))
	spec.sort()
	return spec

def output(pep):
	p = ""
	for x in pep:
		p += str(x) + '-'
	print(p[:-1])

def score(peptide, spectrum):
	spec = linSpec(peptide)
	score = 0
	i = 0
	for x in spectrum:
		for y in range(i,len(spec)):
			if x == spec[y]:
				score +=1
				i = y+1
				break
	return score

def cScore(peptide, spectrum):
	spec = cycSpec(peptide)
	score = 0
	i = 0
	for x in spectrum:
		for y in range(i,len(spec)):
			if x == spec[y]:
				score +=1
				i = y+1
				break
	return score

def cut(leaderboard, spectrum, n):
	if len(leaderboard) <= n:
		return leaderboard
	scores = []
	for x in leaderboard:
		scores.append(cScore(x, spectrum))
	scores.sort()
	scores.reverse()
	min = scores[n-1]
	new = []
	for x in leaderboard:
		if cScore(x, spectrum) >= min:
			new.append(x)
	return new

def LCS(spectrum, n):
	lboard = [[]]
	lpeptide = []
	lscore = 0
	while lboard != []:
		lboard = expand(lboard)
		newleaderboard = []
		for pep in lboard:
			if sum(pep) == spectrum[-1]:
				if cScore(pep, spectrum) >= lscore:
					lpeptide = pep
					lscore = cScore(pep, spectrum)
			if sum(pep) <= spectrum[-1]:
				newleaderboard.append(pep)
		lboard = cut(newleaderboard,spectrum, n)
	return lpeptide

output(LCS(spectrum, n))