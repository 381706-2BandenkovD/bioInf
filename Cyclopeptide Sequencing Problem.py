MASS = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
def ParentMass(Spectrum):
    return max(Spectrum)

def expand(peptide_lst):
    expanded_peptide_lst = []
    for peptide in peptide_lst:
        for aminoacid in MASS:
            expanded_peptide_lst.append(peptide + [aminoacid])
    return expanded_peptide_lst


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

#ip = "0 99 101 103 113 113 114 128 163 204 212 216 227 227 227 264 291 317 326 330 340 340 367 390 392 431 439 443 454 480 491 495 503 542 544 567 594 594 604 608 617 643 670 707 707 707 718 722 730 771 806 820 821 821 831 833 835 934"
#Spectrum = list(map(int, ip.split()))
#Spectrum = [0, 113, 128, 186, 241, 299, 314, 427]

peptides = input()
Spectrum = [int(number) for number in peptides.split(' ')]

peptides = [[]]
while peptides != []:
	peptides = expand(peptides)
	tmp_list = []
	for pep in peptides:
		if sum(pep) == ParentMass(Spectrum):
			spec = cycSpec(pep)
			if len(spec) == len(Spectrum):
				couter = True
				for i in range(len(spec)):
					if spec[i] != Spectrum[i]:
						couter = False
						break;
				if couter:
					print('-'.join(map(str,pep)))
		else:
			spec = linSpec(pep)
			couter = True
			i = -1
			for x in spec:
				coterx = False
				for y in range(i+1,len(Spectrum)):
					if x==Spectrum[y]:
						coterx = True
						i = y
						break;
				if coterx == False:
					couter = False
					break;
			if couter:
					tmp_list.append(pep)
	peptides = tmp_list