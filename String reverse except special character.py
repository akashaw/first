import re
a=input()
dict={}
for i in range(len(a)):
    if not((65 <= ord(a[i]) <= 90 ) or ( 97 <= ord(a[i]) <= 122 ) or ( 48 <= ord(a[i]) <= 57)): #selects all except alphabet and digits
        dict[i]=a[i]
str=re.findall("[a-zA-Z]",a)
str.reverse()
for i in dict:
    str.insert(i,dict[i])
print(str)