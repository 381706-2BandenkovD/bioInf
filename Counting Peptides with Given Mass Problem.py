from collections import Counter
from math import factorial

def pepMas(mass, recursive=False):
    amin = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'L', 'N', 'D', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    weight = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    return recursPepMas(weight, amin, mass, '')

def recursPepMas(weight, amin, mass, peptide):
    if len(weight) == 0 and mass > 0:
        return 0
    elif mass < 0:
        return 0
    elif mass == 0:
        count = Counter(peptide)
        div = 1
        for v in count.values():
            div *= factorial(v)
        return factorial(len(peptide))/div
    else:
        return recursPepMas(weight, amin, mass - weight[0], peptide + amin[0]) + \
               recursPepMas(weight[1:], amin[1:], mass, peptide)
MassA = int(input())
print(int(pepMas(MassA)))