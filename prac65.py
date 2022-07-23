# 멀쩡한 사각형

# 내 풀이
def GCD(h, w):
    while w :
        h, w = w, h % w
    return h

def solution(w, h):
    answer = 1
    
    if w > h:
        h, w = w, h
    
    gcd = GCD(h, w)
    
    answer = w * h - (w + h - gcd)
    
    return answer

w = 8
h = 12
print(solution(w,h)) # 80

# 다른 사람 풀이 1
def gcd(a,b): return b if (a==0) else gcd(b%a,a)    
def solution(w,h): return w*h-w-h+gcd(w,h)

# 다른 사람 풀이 2
from math import gcd
def solution(w,h):
    return w * h - (w/gcd(w, h) + h/gcd(w, h) - 1) * gcd(w, h)