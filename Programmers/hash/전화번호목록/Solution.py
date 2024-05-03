def solution(phone_book):
    answer = True
    store = {}
    phone_book.sort()

    for phone_num in phone_book:
        num = phone_num
        temp = ""
        for prev in num:
            temp += prev
            if temp in store:
                answer = False
        
        if answer:
            store[phone_num] = 1
        else:
            break

    return answer

arr = input().split()
print(solution(arr))