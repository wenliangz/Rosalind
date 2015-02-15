from collections import defaultdict #this will make your life simpler
f = open('rosalind_gc.txt','r')
seq_dict=defaultdict(str)
name = ''
for line in f:
    #if your line starts with a > then it is the name of the following sequence
    if line.startswith('>'):
        name = line[1:-1]
        continue #this means skips to the next line
    #This code is only executed if it is a sequence of bases and not a name.
    seq_dict[name]+=line.strip()
max_name=""
max_GC=0
for key,value in seq_dict.iteritems():
	n=0
	lenth=len(value)
	for base in value:
		if base=="G" or base=="C":
			n+=1
	ptg_GC=float(n)*100/lenth
	seq_dict[key]=str(n*100/lenth)+"%"
	if ptg_GC>max_GC:
		max_GC=ptg_GC
		max_name=key
print seq_dict
print "The max GC content seq is:\n", max_name+"\n","%.6f" % max_GC
