# N개의 최소공배수


def get(a, b):
    if b > a:
        a, b = b, a
    
    while True:
        a, b = b, a % b
        if b == 0:
            break
    return a


def solution(arr):
    answer = 1

    while len(arr) != 1:
        a = arr.pop()
        b = arr.pop()
        
        gcd = get(a, b)
        
        result = a * b / gcd
        arr.append(int(result))
    
    answer = arr[0]
    
    return answer

arr = [2,6,8,14]
print(solution(arr)) # 168

