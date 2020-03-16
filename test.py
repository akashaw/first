from itertools import product as p
a=(input())
print(a)
b=list(p(a,repeat=10))
for i in b:
	print(''.join(i))
print(len(b))
