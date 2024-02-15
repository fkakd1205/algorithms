from sys import stdin

# 트라이 알고리즘
class Node:
    def __init__(self, key=None):
        self.key = key
        self.child = dict()

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, s):
        cur = self.root
        for c in s:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]

    def find(self, s):
        cur = self.root
        for c in s:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return True
    
trie = Trie()
N, M = map(int, input().split())

for _ in range(N):
    s = comp = stdin.readline().rstrip()
    trie.insert(s)

count = 0
for _ in range(M):
    comp = stdin.readline().rstrip()
    if trie.find(comp):
        count += 1

print(count)
