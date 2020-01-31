hi=input()
hi=hi.split(',')
ans=[]
for a in hi:
    l = a.split(':')
    string = l[0]
    length = len(string)
    code = (l[1])
    code = list(code)
    code.sort()
    new_code = []
    for i in code:
        if int(i) <= length:
            new_code.append(i)
    if len(new_code) == 0:
        element = 'X'
    else:
        index = int(new_code[-1]) - 1
        element = string[index]
    ans.append(element)
print(''.join(ans))