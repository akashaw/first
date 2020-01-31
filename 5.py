n=int(input())
arr=list(map(int,input().split(",")))
arr=arr[n:]
ans=0
temp=[]
for i in arr:
    if i not in temp:
        ans+=1
        temp.append(i)

print(ans)
