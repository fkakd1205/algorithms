from collections import Counter

def solution(want, number, discount):
    answer = 0
    st = 0
    en = 10
    while True:
        prod = discount[st:en]
        if en > len(discount): break
        prod = Counter(prod)

        sign_up = True
        for product, num in zip(want, number):
            if prod[product] < num:
                sign_up = False
                break
        if sign_up:
            answer += 1

        st += 1
        en += 1
    return answer

want = input().split()
number = list(map(int, input().split()))
discount = input().split()
print(solution(want, number, discount))

