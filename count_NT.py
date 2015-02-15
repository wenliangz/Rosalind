DNA=open('/Volumes/DATA/documents/bioinformatics/Rosalind/rosalind_dna.txt')
#print DNA.readline()
a=0
c=0
g=0
t=0
for X in DNA.readline():
	if X =='A':
		a=a+1
	if X =='C':
		c=c+1
	if X =='G':
		g=g+1
	if X =='T':
		t=t+1
print a,c,g,t