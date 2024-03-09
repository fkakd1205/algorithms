from sys import stdin

N = int(input())
students = [list(stdin.readline().split()) for _ in range(N)]

students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for name, k, e, m in students:
    print(name)
