import re
a='Hello#81@21349'
b=re.findall("\d",a)
b.sort(reverse=True)
c=[];d=[]
for i in range(len(b)):
    if int(b[i])%2==0:
        c.append(b[i])
    if b[i] not in d:
        d.append(b[i])
if len(c)==0:
    print(-1)
else:
    temp=c.pop(-1)
    d.remove(temp)
    d.append(temp)
    print(''.join(d))