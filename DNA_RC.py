DNA=open('/Volumes/DATA/documents/bioinformatics/Rosalind/rosalind_revc.txt')
#print DNA.readline()
reverse=DNA.readline()[::-1].strip()
compliment={'A':'T','C':'G','G':'C','T':'A'}
letters=list(reverse)
print letters
RC=[compliment[base] for base in letters]
print RC
RCDNA=''.join(RC)
print RCDNA