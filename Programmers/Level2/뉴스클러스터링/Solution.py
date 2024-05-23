def get_seperated_str(str):
    store= dict()
    for i in range(len(str) - 1):
        sep = str[i:i+2]
        if sep in store:
            store[sep] += 1
        else:
            store[sep] = 1

    return store

def solution(str1, str2):
    answer = 0
    a = 0   # 교집합
    b = 0   # 합집합
    str1 = str1.lower()
    str2 = str2.lower()

    store1 = get_seperated_str(str1)
    store2 = get_seperated_str(str2)
    
    for sep in store1:
        if not sep.isalpha(): continue
        if sep in store2:
            a += min(store1[sep], store2[sep])
            b += max(store1[sep], store2[sep])
            store1[sep] = 0
            store2[sep] = 0

    for sep in store1:
        if not sep.isalpha(): continue
        b += store1[sep]

    for sep in store2:
        if not sep.isalpha(): continue
        b += store2[sep]
    
    if a + b == 0:
        answer = 1
    else:
        answer = a / b
    
    answer *= 65536
    return int(answer)

str1 = input().rstrip()
str2 = input().rstrip()
print(solution(str1, str2))

# V2.
def solution2(str1, str2):
    answer = 0
    store1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str(str1[i:i+2]).isalpha()]
    store2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str(str2[i:i+2]).isalpha()]

    gyo = set(store1) & set(store2)     # 교집합
    hap = set(store1) | set(store2)     # 합집합

    gyo_sum = sum([min(store1.count(g), store2.count(g)) for g in gyo])
    hap_sum = sum([max(store1.count(h), store2.count(h)) for h in hap])

    if hap_sum == 0:
        answer = 65536
    else:
        answer = (gyo_sum / hap_sum) * 65536

    return int(answer)

str1 = input().rstrip()
str2 = input().rstrip()
print(solution2(str1, str2))
