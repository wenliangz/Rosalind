a=4940
b=9702
l=range(a,b+1)
y=[]
for x in l:
	if x%2==1:
		y=[x].append([x])
print sum(y)