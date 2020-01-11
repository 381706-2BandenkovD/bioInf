from collections import Counter
text = str(input())
k = int(input())
words = Counter(text[i:i+k] for i in range(len(text) - k + 1))  
d = dict(words.most_common())  
max_value = max(d.values())
fd = {k: v for k, v in d.items() if v == max_value}
for key in fd.keys():
    print(key)