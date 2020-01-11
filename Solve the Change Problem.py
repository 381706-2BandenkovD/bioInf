money = int(input())
coins = list(map(int, input().split(',')))

result = []
for i in coins:
	if money % i == 0:
		result.append(money / i)
coi = {}
while money != 0:
	coi[max(coins)] = money // max(coins)
	money = money % max(coins)
	coins.remove(max(coins))
result.append(sum(coi.values()))
print(int(min(result)))