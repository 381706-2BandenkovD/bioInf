str2 = str(input())
str1 = str(input())
m = len(str1)
n = len(str2)
tmpMtr = [[0] * (n + 1) for i in range(m + 1)]
podstr = ''
if m == 0 or n == 0:
	print(podstr)
else:
	for i in range(1, m+1):
		for j in range(1, n+1):
			if str1[i-1] == str2[j-1]:
				tmpMtr[i][j] = tmpMtr[i-1][j-1] + 1
								
			else:
				if tmpMtr[i-1][j] >= tmpMtr[i][j-1]:
					tmpMtr[i][j] = tmpMtr[i-1][j]
				else:
					tmpMtr[i][j] = tmpMtr[i][j-1]

t = tmpMtr[m][n]
for i in range(m):
	for j in range(n):
		if str1[m-i-1] == str2[n-j-1] and tmpMtr[m-i][n-j] == t:
			podstr += str1[m-i-1]
			t -= 1
			break
				
result = ''
for i in range(len(podstr)):
	result += podstr[len(podstr)-i-1]
print(result)