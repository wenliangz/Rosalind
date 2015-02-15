#!/usr/bin/env python
DNA=open('/BootStrappers@Umass/Rosalind/rosalind_dna.txt')
seq=DNA.readlines()[0].strip()
print seq
# a=0
# c=0
# g=0
# t=0
# for X in DNA.readline():
# 	if X =='A':
# 		a=a+1
# 	if X =='C':
# 		c=c+1
# 	if X =='G':
# 		g=g+1
# 	if X =='T':
# 		t=t+1
# print a,c,g,t


class DNASequence(object):
	def __init__(self,sequence):
		self.sequence = sequence
	def count(self):
		base_count={'A':0,'C':0,'G':0,'T':0}
		for letter in self.sequence:
			base_count[letter]+=1
		return base_count
	def transcribe(self):

my_sequence=DNASequence(seq)
my_count=my_sequence.count()
