def func(x):
    name=list(x.split(':')[0])
    number=list(map(int,x.split(':')[1]))
    number.sort(reverse=True)
    n=len(name)
    if int(n) in number:
        return (name[n-1])
    else:
        for i in number:
            condition=i<n
            if condition:
                return (name[i-1])
        if not condition:
             return 'X'


ini='Robert:36787,Tina:68721,Jo:56389'
emp=ini.split(',')
ans=''
for i in emp:
    temp=func(i)
    ans=ans+str(temp)
print(ans)
