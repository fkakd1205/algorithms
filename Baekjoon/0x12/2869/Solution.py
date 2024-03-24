A, B, V = map(int, input().split())

# 도착 날 x
# Ax - B(x-1) = V
# x = (V - B) / (A - B)
# 하루가 지났을 때(A-B)
# V-B까지 도달했다면 A > B이므로 V까지 도착한 것이다.
x = (V - B) // (A - B)

if (V - B) % (A - B) == 0:
    print(x)
else:
    print(x+1)  # 나머지가 있다는건 x일에서 하루 더 가야 도착할 수 있다
