import re
def maxeven(string):
    lis=re.findall('\d',string)
    lis.sort()
    lis.reverse()
    for i in lis:
        i=int(i)
        if i%2==0:
            return i
        elif i==int(lis[-1]):
            return -1

print(maxeven('infytq73119755'))