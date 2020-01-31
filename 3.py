iseven=lambda x:x%2==0

a='t9@a42&516'
b=list('~!@#$%^&*()_+{}|:<>?`-=[]\;,./')
a=list(a)
s_c=0;  even=[];    odd=[]; ans=[]
for i in a:
    if i in b:
        s_c+=1
    if i.isdigit():
        if iseven(int(i)):
            even.append(i)
        else:
            odd.append(i)

for i in range(min(len(even),len(odd))):
    if iseven(s_c):
        ans.append(even[i])
        ans.append(odd[i])
    else:
        ans.append(odd[i])
        ans.append(even[i])

if not (iseven(len(even)+len(odd))):
    if iseven(s_c):
        ans.append(even[-1])
    else:
        ans.append(odd[-1])
print(''.join(ans))

