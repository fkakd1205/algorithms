def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)

def is_divided(arr, n):
    for num in arr:
        if num % n == 0:
            return True
        
    return False

def solution(arrayA, arrayB):
    answer = 0
    gcdA = arrayA[0]
    gcdB = arrayB[0]

    for num in arrayA:
        gcdA = gcd(gcdA, num)
    
    for num in arrayB:
        gcdB = gcd(gcdB, num)

    if is_divided(arrayB, gcdA):
        gcdA = 0
    if is_divided(arrayA, gcdB):
        gcdB = 0

    answer = max(gcdA, gcdB)
    return answer

arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))
print(solution(arrayA, arrayB))
