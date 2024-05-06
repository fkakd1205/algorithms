def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        sorted_array = sorted(array[i-1:j])
        answer.append(int(sorted_array[k-1]))

    return answer

N = int(input())
array = input().split()
commands = [list(map(int, input().split())) for _ in range(N)]
print(solution(array, commands))
