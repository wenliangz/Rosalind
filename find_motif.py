seq=[]
with open('rosalind_subs.txt') as f:
	for each in f:
		each=each.strip()
		seq.append(each)
#print seq
temp=seq[0]
motif=seq[1]
#print temp
#print motif

lenth_motif=len(motif)
lenth_temp=len(temp)
n=0
for i in xrange(0,lenth_temp-lenth_motif):
	DNA=temp[i:lenth_motif+i]
	#print DNA
	if DNA==motif:
		n+=1
print n