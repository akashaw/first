from itertools import permutations as p
a=(input())
print(a)
b=list(p(a,len(a)))
for i in b:
    print(''.join(i))