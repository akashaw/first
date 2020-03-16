a=str(int(input())+1)
rev_a=a[::-1]
l=len(a)
if l%2==0:
    temp=a[:l//2]
    temp=temp+temp[::-1]
    if int(a)>int(temp):
        temp=str(int(a[:l//2])+1)
        temp=temp+temp[::-1]
else:
    temp=a[:l//2]
    temp=temp+a[l//2:l//2+1]+temp[::-1]
    if int(a)>int(temp):
        temp=str(int(a[:l//2+1])+1)
        temp=temp+str(temp[:l//2])[::-1]
print(temp)
