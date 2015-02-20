#!/usr/bin/env python
from collections import defaultdict
import argparse, sys

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--fasta', action="store_true", default=False)
	parser.add_argument('--file', type=str)
	parser.add_argument('--target', type=str)
	parser.add_argument('--function', type=str)
	parser.add_argument('remainingArguments', type=str, nargs='*') # dump all the other arguments in a string list
	return parser.parse_args()
#[FASTA/seq] [target seqence [1,2,3...]/all] [function]



class DNASequence(object):
	# add default attributes to classe and keyword arguments
	def __init__(self,sequence, name = None):
		self.sequence = sequence
		self.name = name

	# def __repr__(self):
	# 	if self.name is None:
	# 		return "Unknown " + str(self.gc_content())
	# 	return self.name + " " + str(self.gc_content())

	#problem 1: Base count
	def countbase(self):
		# define a default dict to avoid keywork error in the case that some bases may not be existingin the sequence
		base_count=defaultdict(int)
		for letter in self.sequence:
			base_count[letter]+=1
		return base_count

	#problem 2: RNA
	def transcribe(self):
 		new_rna=self.sequence.replace('T','U')
 		return new_rna

 	#Problem 3: REVC
 	def reverseComplement(self):
 		reverse=self.sequence[::-1]
		compliment={'A':'T','C':'G','G':'C','T':'A'}
		letters=list(reverse)
		RC=[compliment[base] for base in letters]
		RCDNA=''.join(RC)
		return RCDNA

	#Problem 4: GC content	
	def gc_content(self):
		counts=self.countbase()
		gc=counts['G']+counts['C']
		gc_percent=float(gc)/len(self.sequence)
		return gc_percent

	def Hamm(self,new_sequence): #new_sequence need to be an sequence object input
		#print type(new_sequence)
		seq1_dict={}
		seq2_dict={}
		for position,base in enumerate(self.sequence):
			seq1_dict[position]=base
		for position,base in enumerate(new_sequence.sequence):
			seq2_dict[position]=base
		seq1_set=set(seq1_dict.iteritems())
		seq2_set=set(seq2_dict.iteritems())
		Hamm=seq1_set-seq2_set
		return len(Hamm)

	def FindMotif(self,motif_Obj):
		lenth_temp=len(self.sequence)
		lenth_motif=len(motif_Obj.sequence)
		n=0
		p=[]
		for i in xrange(0,lenth_temp-lenth_motif):
			DNA=self.sequence[i:lenth_motif+i]
			#print DNA
			if DNA==motif_Obj.sequence:
				n+=1
				p.append(i+1)
		return n,p

	def RNASplicing(self,intron_obj_list):
		# n=len(intron_obj_list)
		# while n>0:
		# 	len_preRNA=len(self.sequence)
		# 	#print len_preRNA
		# 	len_intron=len(intron_obj_list[n-1].sequence)
		# 	#print len_intron, intron_obj_list[n-1].sequence
		# 	for i in xrange(0,len_preRNA-len_intron+1):
		# 		RNA=self.sequence[i:len_intron+i]
		# 		#print RNA
		# 		if RNA==intron_obj_list[n-1].sequence:
		# 			self.sequence=self.sequence[0:i]+self.sequence[(len_intron+i):] 
		# 			#try replace() function too here
			# n-=1
		for intron in intron_obj_list:
			self.sequence=self.sequence.replace("intron","")
			
		#print self.sequence
		mRNA=DNASequence(self.sequence).transcribe()
		#print mRNA
		protein=RNASequence(mRNA).translate()
		#print protein
		return protein

	def REVP(self):
		revp_list=[]
		for n in xrange(4,13,2):
			for i in xrange(0,len(self.sequence)-n+1):
				seg=self.sequence[i:i+n]
				if seg==DNASequence(seg).reverseComplement():
					revp_list.append([i+1,n])
		for unit in revp_list:
			print " ".join(map(str,unit))
		return revp_list


	
#Define a new classs for RNA sequence input
class RNASequence(object):
	def __init__(self, RNAseq):
		self.RNAseq=RNAseq
		self.codon_dict=defaultdict(str)
		with open("codon_table.txt") as f:
			for each in f:
				toks = each.split()
				self.codon_dict[toks[0]] = toks[1]
	def translate(self):
		codon_list=[]
		codon=[n for n in xrange(0,len(self.RNAseq),3)]
		for i in codon:
			if self.codon_dict[self.RNAseq[i:i+3]]=="STOP":
				break
			codon_list.append(self.codon_dict[self.RNAseq[i:i+3]])
		protein=''.join(codon_list)
		#protein=protein.replace('STOP','')
		return protein
	

#Define a class to parse FASTA files or sequence files seperated by enter into DNA or RNA sequence object
class ParseFile(object):
	def __init__(self,pfn):
		self.pfn=pfn
	def FASTA(self): # Method2 for parsing fasta file into DNASequence object
		found_sequences=[]
		with open(self.pfn,'r') as input:
			sequence=''
			for i,line in enumerate(input):
				if i==0:
					name=line.rstrip('\n').lstrip('>')
				else:
					if line.startswith('>'):
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

	def Seq(self): # Method for parsing DNA sequence file into DNASequence object
		SeqObj=[]
		with open(self.pfn) as f:
			whole_sequence="".join(f.readlines()).strip()
			f.seek(0)
			for line in f:
				line=line.strip()
				if "U" in whole_sequence:
					SeqObj.append(RNASequence(line)) #append DNA sequence object instead of sequence itself
				else:
					SeqObj.append(DNASequence(line)) #append RNA sequence object instead of sequence itself
		return SeqObj

	#def RNAseq(self): # Method for parsing RNA sequence file into DNASequence object
		#RNA_objects=[]
		#with open(self.pfn) as f:
			#for line in f:
				#line=line.strip()
				#RNA_objects.append(RNAsequence(line))  #append sequence object instead of sequence itself
		#return RNA_objects


if __name__ == '__main__':  # Run the following code only when the code is runing as a main program, but not when it is called by other script. 

#parameters: --file [filenamename] [FASTA/seq] [target seqence [1,2,3...]/all] [function]
	if not args.fasta:
		print "ERROR: please specify format (options: --fasta, --fastq, ...)"
		sys.exit(1)
	if not args.target:
		print "ERROR: please specify target (options: 1, 2, ... or all)"
		sys.exit(1)
	allowedFunctions = ['RNASplicing', 'otherfunction']
	if not args.function in allowedFunctions:
		print "ERROR: allowed funtions are:", allowedFunctions
		sys.exit(1)

	if args.remainingArguments[0]=="fasta":
		s=ParseFile(args.file).FASTA()  
	elif args.remainingArguments[0]=="seq":
		s=ParseFile(args.file).Seq()
	else: 
		print "please input sequence format(fasta/seq)!"
	
	if args.remainingArguments[2]=="translate":
		seq_number=args.remainingArguments[1].split(',')
		for each in seq_number:
			print s[int(each)-1].translate()
	elif args.remainingArguments[2]=="gc":
		seq_number=args.remainingArguments[1].split(',')
		for each in seq_number:
			print s[int(each)-1].gc_content()
	elif args.remainingArguments[2]=="transcribe":
		seq_number=args.remainingArguments[1].split(',')
		for each in seq_number:
			print s[int(each)-1].transcribe()
	elif args.remainingArguments[2]=="REVC":
		seq_number=args.remainingArguments[1].split(',')
		for each in seq_number:
			print s[int(each)-1].reverseComplement()
	elif args.remainingArguments[2]=="hamm":
		seq_number=args.remainingArguments[1].split(',')
		seq1=s[int(seq_number[0])-1]
		seq2=s[int(seq_number[1])-1]
		print seq1.Hamm(seq2)
	elif args.remainingArguments[2]=="motif":
		seq_number=args.remainingArguments[1].split(',')
		temp=s[int(seq_number[0])-1]
		motif=s[int(seq_number[1])-1]
		print temp.FindMotif(motif)
	elif args.remainingArguments[2]=="RNASplicing" and args.remainingArguments[1]=="all":
		preRNA=s[0]
		introns=s[1:]
		print preRNA.RNASplicing(introns)
	elif args.remainingArguments[2]=="revp":
		seq_number=args.remainingArguments[1].split(',')
		for each in seq_number:
			print s[int(each)-1].REVP()



