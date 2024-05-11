def solution(people, limit):
    answer = 0
    # 투포인터
    st = 0
    en = len(people) - 1
    people.sort()   # 가벼운 사람과 무거운 사람을 같이 태우기 위해 정렬
    
    while(True):
        if st > en: break

        # st와 en의 무게가 limit을 넘는다면 횟수 추가
        while(st < en and people[st] + people[en] > limit):
            answer += 1
            en -= 1
        
        if st <= en:
            st += 1
            en -= 1
            answer += 1

    return answer

people = list(map(int, input().split()))
limit = int(input())
print(solution(people, limit))
