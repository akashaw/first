hi=(list(input()))
new=[]
for i in range(len(hi)):
    if i%2!=0:
        temp=int(hi[i])
        new.append(temp*temp)
ans=''.join(map(str,new))
ans=ans[:4]
print(ans)