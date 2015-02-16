#!/usr/bin/env python
from collections import defaultdict
DNA=open('/BootStrappers@Umass/Rosalind/rosalind_dna.txt')
seq=DNA.readlines()[0].strip()
class DNASequence(object):
	def __init__(self,sequence, name = None):
		self.sequence = sequence
		self.name = name

	def __repr__(self):
		if self.name is None:
			return "Unknown " + str(self.gc_content())
		return self.name + " " + str(self.gc_content())

	def count(self):
		base_count=defaultdict(int)#{'A':0,'C':0,'G':0,'T':0}
		for letter in self.sequence:
			base_count[letter]+=1
		return base_count

	def transcribe(self):
 		new_rna=self.sequence.replace('T','U')
 		return new_rna
 	
 	def reverseComplement(self):
 		reverse=self.sequence[::-1]
		compliment={'A':'T','C':'G','G':'C','T':'A'}
		letters=list(reverse)
		RC=[compliment[base] for base in letters]
		RCDNA=''.join(RC)
		return RCDNA
	def gc_content(self):
		counts=self.count()
		gc=counts['G']+counts['C']
		gc_percent=float(gc)/len(self.sequence)
		return gc_percent
	

class FASTAFile(object):
	def __init__(self,path):
		self.path=path

	def seuqence(self):
		found_sequences=[]
		with open(self.path,'r') as input:
			sequence=''
			for i,line in enumerate(input):
				if i==0:
					name=line.rstrip('\n').lstrip('>')
				else:
					if line.startwith('>'):
						new_sequence_object=DNASequence(sequence,name)
						found_sequences.append(new_sequence_object)
						sequence=''
						name=line.rstrip('\n').lstrip('>')
					else:
						sequence+=line.rstrip('\n')
			else:
				new_sequence_object=DNASequence(sequence,name)
				found_sequences.append(new_sequence_object)
		return found_sequences


my_sequence=DNASequence(seq)
print my_sequence
my_count=my_sequence.count()
my_RNA=my_sequence.transcribe()
my_REVC=my_sequence.reverseComplement()
#print my_REVC


mylist = [DNASequence("ATCCCG", "sequence 1"), DNASequence("AAAAATTTT", "sequence 2")]
for seq in mylist:
	print seq
#sidebargit test
