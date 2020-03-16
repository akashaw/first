from math import sqrt

a=list(map(int,'6,3,6,20,3,6,-15,3,3'.split(',')))
new_a=[]
temp=[]
l=int(sqrt(len(a)))
res=[]
i_lis=[]
s=[]
s1=[]

def printmatrix(i, size):
    for x in range(int(sqrt(size))):
        for y in range(int(sqrt(size))):
            print(i[x*int(sqrt(size))+y], end=' ')
        print('')

for i in range(l-1,-1,-1):
    i=(i+1)
    i_lis.append(i)

for i in i_lis:
    i=i**2
    temp=[]
    for k in range(len(a) - i + 1):
        temp1=[]
        for j in range(i):
            x = a[j+k]
            temp1.append((x))
        temp.append(temp1)
    new_a.append(temp)



for i in new_a:
    s=[]
    for j in i:
        #print(j)
        s.append(sum(j))
    s1.append(s)

#print(new_a) the new matrix
#print(s1) the matrix containing sum
#print(max(max(s1))) the max sum

for i in new_a:
    for j in i:
        if sum(j)==max(max(s1)):
            #print(j)
            printmatrix(j, len(j))