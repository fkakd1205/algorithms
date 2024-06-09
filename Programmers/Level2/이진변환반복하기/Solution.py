def solution(s):
    answer = []
    ex_cnt = 0
    rm_cnt = 0

    while s != '1':
        if ex_cnt > 5: break
        ex_cnt += 1
        new_s = ''
        for bit in str(s):
            if bit == '0':
                rm_cnt += 1
                continue
            new_s += bit
        
        new_s = len(new_s)
        s = bin(new_s)[2:]

    answer = [ex_cnt, rm_cnt]
    return answer

s = input()
print(solution(s))
