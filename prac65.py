# 멀쩡한 사각형

def solution(w,h):
    answer = 1
    
    if w > h:
        w, h = h, w
        
    return answer

w = 8
h = 12
print(solution(w,h)) # 80