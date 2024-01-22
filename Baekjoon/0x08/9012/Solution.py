from sys import stdin

T = int(input())

for _ in range(T):
    command = stdin.readline().rstrip()
    stack = []

    for chr in command:
        if(chr == '('):
            stack.append(chr)
        elif(chr == ')'):
            if(len(stack) == 0):
                stack.append(chr)
                break
            else:
                comp_chr = stack.pop()
                if(comp_chr != '('):
                    stack.append(chr)
                    break
    
    if(len(stack) == 0):
        print("YES")
    else:
        print("NO")
