def lonPathInManh(n, m, down, right):
	res = [[0] * (m+1) for i in range(n+1)]
	for i in range(1,n+1):
		res[i][0] = res[i-1][0] + int(down[i-1][0])
	for j in range(1,m+1):
		res[0][j] = res[0][j-1] + int(right[0][j-1])
	for i in range(1,n+1):
		for j in range(1,m+1):
			res[i][j] = max(res[i-1][j] + int(down[i-1][j]), res[i][j-1] + int(right[i][j-1]))
	return res[n][m]

n, m = map(int, input().split(" "))
matrix = []
down = []
right = []
flag = 1
while (flag):
    try:
        matrix.append(str(input()).replace(' ', ''))
    except EOFError:
        flag = 0
fl = 0
for i in matrix:
    if (i != '-') & (fl == 0):
        down.append(i)
    else:
        fl =1
        right.append(i)
right.pop(0)
print(lonPathInManh(n,m,down,right))