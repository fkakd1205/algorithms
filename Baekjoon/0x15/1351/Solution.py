N, P, Q = map(int, input().split())
store = dict()
store[0] = 1

def solve(n):
    if n in store:
        return store[n]
    else:
        store[n] = solve(n // P) + solve(n // Q)
        return store[n]
    
print(solve(N))
