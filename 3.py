
string='t24613579@a&'

even=[]
odd=[]
special_char=0
for ch in string:
    if(ch.isalnum() == False):
        special_char+=1
    elif(ch.isdigit()):
        if int(ch)%2==0:
            even.append(ch)
        else:
            odd.append(ch)

if(special_char%2!=0):
      odd,even=even,odd
even_len=len(even)
odd_len=len(odd)
m=max(even_len,odd_len)
print(even,odd,even_len,odd_len,m)
e=0
o=0
for i in range(m):
    if(e!=even_len):
        print(even[e],end='')
        e+=1
    if(o!=odd_len):
        print(odd[o],end='')
        o+=1
