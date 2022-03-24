

import math

def isprime(number):
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def solution(n):
    answer = 0
    for i in range(2,n+1):
        if isprime(i) :
            answer += 1
    return answer


