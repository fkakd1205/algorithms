from sys import stdin

# ==============================
# V1. 시간초과 (트라이 알고리즘. 2차원 배열)
# N, M = map(int, input().split())
# MAX = N * 500 + 5   # 문자열 개수 N * 최대 길이 500
# next = [list([-1] * 26) for _ in range(MAX)]    # (문자열 개수 N * 최대 길이 500) 사이즈에서 알파벳 개수 만큼 할당

# ROOT = 1
# unused = 2
# check = [False] * MAX

# def c2i(c):
#     return ord(c) - ord('a')

# def insert(s):
#     global unused

#     cur = ROOT
#     for c in s:
#         if next[cur][c2i(c)] == -1:
#             next[cur][c2i(c)] = unused
#             unused += 1
#         cur = next[cur][c2i(c)]
#     check[cur] = True

# def find(s):
#     cur = ROOT
#     for c in s:
#         if next[cur][c2i(c)] == -1:
#             return False
#         cur = next[cur][c2i(c)]
#     return check[cur]

# S = [stdin.readline().rstrip() for _ in range(N)]
# comp = [stdin.readline().rstrip() for _ in range(M)]

# for s in S:
#     insert(s)

# count = 0
# for cp in comp:
#     if find(cp):
#         count += 1

# print(count)

# ==============================
# V2. 시간초과 (트라이알고리즘, 딕셔너리)
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.childrun = dict()
    
# class Trie:
#     def __init__(self):
#         self.root = Node(None)

#     def insert(self, s):
#         cur = self.root
#         for c in s:
#             if c not in cur.childrun:
#                 cur.childrun[c] = Node(c)
#             cur = cur.childrun[c]
    
#     def find(self, s):
#         cur = self.root
#         for c in s:
#             if c not in cur.childrun:
#                 return False
#             cur = cur.childrun[c]
#         return True if len(cur.childrun) == 0 else False

# N, M = map(int, input().split())
# trie = Trie()

# for _ in range(N):
#     s = stdin.readline().rstrip()
#     trie.insert(s)

# count = 0
# for _ in range(M):
#     comp = stdin.readline().rstrip()
#     if trie.find(comp):
#         count += 1

# print(count)

# ==============================
# V3. 딕셔너리
N, M = map(int, input().split())
S = {stdin.readline().rstrip() for _ in range(N)}

count = 0
for _ in range(M):
    comp = stdin.readline().rstrip()
    if comp in S:
        count += 1

print(count)
