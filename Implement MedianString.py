import itertools
def getCombo(k):
    bases=['A','T','G','C']
    combo=[''.join(p) for p in itertools.product(bases, repeat=k)]
    return combo

def minHammDist(pattern, string):
	minDist = len(pattern)
	for i in range(len(string) - len(pattern) + 1):
		count = 0
		for j in range(len(pattern)):
			if pattern[j] != string[i:i+len(pattern)][j]:
				count += 1
		if count < minDist:
			minDist = count
	return minDist

k = int(input())
dna = []
#dna = ['GAAACTACGCACGTAGTGTTTTGCTACGGTTCTCA', 'TATATCCACATGACCTCGACAACGCACGGTCGAAT', 'TAGCGGGACAATCAGGTCTGAGTCGACTGTTGTGC', 'TCCTGCCGGTTGCTAACTGTAGACGTTTACCCCTT', 'TCCCTCCCTAACTCTAGGCTACTGTCGTCCGCAGT', 'AGGCAGAAAGACAACGGTAGTAATCTAGAGACCGT', 'CGCTCCACGCAGCTCATAGAACCGTGTTGTTCAAC', 'ACTGTCTCCCGGAAACCATAAACTACTTGGTTTGT', 'GGTTTTCTTGACTGTAATTACAATCCAGGAGACCA', 'ATGTCGCTCTACAGTGAACACGTAACTGTCTTCGG']
flag = 1
while (flag):
    try:
        dna.append(str(input()))
    except EOFError:
        flag = 0
kes = []
pattern = getCombo(k)
dist = {}
minString = len(dna) * len(pattern)
for i in pattern:
	sumDist = 0
	for j in range(len(dna)):
		sumDist += minHammDist(i, dna[j])
	dist[i] = sumDist
	if sumDist < minString:
		minString = sumDist
for result in dist.keys():
    if dist[result] == minString:
        kes.append(result)
        break
val = ' '.join(kes)
print(val)