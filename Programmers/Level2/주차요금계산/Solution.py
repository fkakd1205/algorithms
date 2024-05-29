from math import ceil

ONE_MINUTES = 60

# 차량 번호 별 이용시간 구하기
def get_parking_time(records):
    store = dict()
    in_store = dict()
    out_store = dict()

    for record in records:
        time, num, info = record.split()
        h, m = map(int, time.split(":"))
        time = (h * ONE_MINUTES) + m
        if info == 'IN':
            in_store[num] = time
        else:
            out_store[num] = time
            
            if num not in store:
                store[num] = out_store[num] - in_store[num]
            else:
                store[num] += (out_store[num] - in_store[num])
            # 출차했다면 clear
            in_store.pop(num)
            out_store.pop(num)

    # 출차하지 않은 차량 default 출차시간 설정
    for num in in_store:
        time = (23 * ONE_MINUTES) + 59
        if num not in store:
            store[num] = time - in_store[num]
        else:
            store[num] += (time - in_store[num])

    return store

def solution(fees, records):
    answer = []
    store = get_parking_time(records)
    
    sorted_store = sorted(store.items())
    for _, time in sorted_store:
        fee = fees[1]
        if time > fees[0]:
            fee += ceil((time - fees[0]) / fees[2]) * fees[3]
        
        answer.append(fee)

    return answer

fees = list(map(int, input().split()))
n = int(input())
records = [input().rstrip() for _ in range(n)]
print(solution(fees, records))
