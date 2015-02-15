seq=[]
with open('rosalind_hamm.txt') as f:
	for each in f:
		each=each.strip()
		seq.append(each)

seq1=seq[0]
seq2=seq[1]

seq1_dict={}
seq2_dict={}
for position,base in enumerate(seq1):
	seq1_dict[position]=base

for position,base in enumerate(seq2):
	seq2_dict[position]=base

Hamm=set(seq1_dict.iteritems())-set(seq2_dict.iteritems())
dH=len(Hamm)
print dH

