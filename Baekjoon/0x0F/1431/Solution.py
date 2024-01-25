from sys import stdin

N = int(input())
serial_number = [stdin.readline().rstrip() for _ in range(N)]

def digit_sum(num):
    sum = 0
    for chr in num:
        if chr.isdigit():
            sum += int(chr)
    return sum

serial_number.sort(key = lambda x : (len(x), digit_sum(x), x))

print('\n'.join(serial_number))
