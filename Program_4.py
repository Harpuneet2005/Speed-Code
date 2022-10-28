b=[]
x=0
m=0
while len(b)<21:
	x=x+1
	for i in range(2,x//2+1):
		if x%i==0:
			m=m+1
	if m<=0:
		b.append(x)
for i in range(20):
	print(b[i])






















