S=str(input())
MASS={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}

SUBP=[]
s=S+S
for k in range(1, len(S)):
	for j in range(0,len(S)):
		subpep = s[j:j+k]
		SUBP.append(subpep)
SUBP.append(S)

sum=0
SUM=[]
SUM.append(0)
for i in range(0, len(SUBP)):
    st=list(SUBP[i])
    for j in range(0, len(st)):
        sum=sum+MASS[st[j]]
    SUM.append(sum)
    sum=0
SUM.sort()    
for i in range (len(SUM)):
    print(SUM[i])