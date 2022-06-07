# 멀쩡한 사각형


def solution(w,h):
    answer = w * h
    loss = 0
    if w == h:
        loss = w
    else:
        loss = 2 * w
    return answer - loss

w = 8; h = 12
print(solution(w,h))