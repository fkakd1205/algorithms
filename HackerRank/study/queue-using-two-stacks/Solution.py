from sys import stdin

n = int(input())
pop_cnt = 0
right_st = []

for _ in range(n):
    type = stdin.readline().split()
    
    if type[0] == '1':
        right_st.append(int(type[1]))
    elif type[0] == '2':
        pop_cnt += 1
    elif type[0] == '3':
        print(right_st[pop_cnt])
