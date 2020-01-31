def presufix(str):
    for i in range(len(str)//2,0,-1):
        print(i)
        prefix=str[0:i]
        sufix=str[len(str)-i:len(str)]
        if prefix==sufix :
            return prefix

print(presufix('ababadab'))