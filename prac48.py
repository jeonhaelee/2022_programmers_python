# 멀쩡한 사각형
# w * h - (w + h - 최대공약수)

def solution(w,h):
    answer = w * h
    loss = 0
    if w == h:
        loss = w
    elif w > h:
        loss = 2 * h
    else:
        loss = 2 * w
    return answer - loss

w = 4; h = 3
print(solution(w,h))