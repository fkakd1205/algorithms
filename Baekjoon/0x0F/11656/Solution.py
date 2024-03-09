word = input()

arr = []
for i in range(len(word)):
    arr.append(word[i:])

arr.sort()
print(*arr, sep="\n")
