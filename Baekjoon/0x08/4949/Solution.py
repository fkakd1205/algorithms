from sys import stdin

while(True):
    command = stdin.readline().rstrip()
    stack = []
    
    if(command == "."):
        break

    for chr in command:
        if (chr == '(' or chr == '['):
            stack.append(chr)
        elif (chr == ')' or chr == ']'):
            if(len(stack) == 0):
                print("no")
                break

            comp_chr = stack.pop()
            # 괄호 매칭이 실패된 경우
            if(chr == ')' and comp_chr != '(') or (chr == ']' and comp_chr != '['):
                    print("no")
                    break
        
        # 문장이 끝났을 때, 남아있는 괄호가 있는지 검사
        if (chr == '.'):
            if (len(stack) == 0):
                print("yes")
            else:
                print("no")
