from sys import stdin

class Node:
    def __init__(self, key=None):
        self.key = key
        self.child = dict()

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert_and_find(self, s):
        cur = self.root
        for c in s:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
        # 마지막 자리(cur)의 child가 존재한다면 s를 포함하는 숫자가 이미 insert된 것
        return True if len(cur.child) != 0 else False

t = int(input())

for _ in range(t):
    trie = Trie()
    n = int(input())
    arr = list(str(stdin.readline().rstrip()) for _ in range(n))
    arr.sort(key=len, reverse=True)  # 자리수로 내림차순 정렬

    result = "YES"
    for i in range(n):
        if trie.insert_and_find(str(arr[i])):
            result = "NO"
            break

    print(result)
