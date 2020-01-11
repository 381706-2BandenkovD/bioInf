def foundBrother(pattern, mismatch, KMP):
	if mismatch == 0:
		KMP.add(pattern)
	else:
		bases = ['A', 'T', 'C', 'G']
		for i in range(len(pattern)):
			for j in range(len(bases)):
				new_patt = pattern[:i] + bases[j] + pattern[i+1:]
				if mismatch <= 1:
					KMP.add(new_patt)
				else:
					foundBrother(new_patt, mismatch - 1, KMP)

k, d = map(int, input().split(" "))
DNA = []
flag = 1
while (flag):
    try:
        DNA.append(str(input()))
    except EOFError:
        flag = 0

Patterns = []
for n in range(len(DNA)):
	pattern = set()
	for i in range(len(DNA[n]) - k + 1):		
		kmerPatt = set()
		foundBrother(DNA[n][i:i + k], d, kmerPatt)
		for words in kmerPatt:
			pattern.add(words)
	for j in pattern:
		Patterns.append(j)
motifpattern = set()
for element in Patterns:
	if Patterns.count(element) == len(DNA):
		motifpattern.add(element)


RESULT = list(motifpattern)
RESULT.sort()
val = ' '.join(RESULT)
print(val)