def checker(hi):
    x=0
    stack=[]
    for i in hi:
        if i=='(' or i=='[' or i=='{':
            stack.append(i)
            x+=1
            continue
        if len(stack)==0:
            print("extra closing bracket")
            return x+1
        b=stack.pop()
        if (i==')' and b=='(') or (i==']' and b=='[') or (i=='}' and b=='{'):
            x+=1
        else:
            print("pair mismatch")
            return x+1
    if len(stack) == 0:
        print("purely balanced")
        return 0
    else:
        print("opening bracket left")
        return x+1
    #print(first_bracket,second_breacket,third_bracket)

a=input()
print(checker(a))