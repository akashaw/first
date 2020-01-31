def sum_odd(s):
    lis=(s)
    temp=lis[:2]
    lis=lis[2:]+temp
    print(lis)

def sum_even(s):
    lis=(s)
    temp=lis[-1]
    lis=temp+lis[:len(lis)-1]
    print(lis)

def sum_square(n):
    lis=list(map(int,n))
    for i in range(len(lis)):
        lis[i]=lis[i]**2
    return (sum(lis))

#ini=input()
ini='ghftd:1246'
str=ini.split(':')[0]
num=ini.split(':')[1]
a=sum_square(num)

if a%2==0:
    sum_even(str)
else:
    sum_odd(str)

#print(str,a)