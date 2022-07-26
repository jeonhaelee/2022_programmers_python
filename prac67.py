# N개의 최소공배수

# 내 풀이
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

# 다른 사람 풀이 1
from fractions import gcd


def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer

# 다른 사람 풀이 2
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def nlcm(num):
    num.sort()
    max_num = num[-1]
    # print (num, max_num)
    temp = 1
    for i in range(len(num)):
        # lcm = (a*b) / gcd
        # gcd = (a*b) / lcm
        temp = (num[i] * temp) / (gcd(num[i], temp))
        # print (temp)
    return temp