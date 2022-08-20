# 조이스틱
# A를 기준으로 생각하자! 위아래와 좌우로.

def solution(name):
    answer = 0
    min_move = len(name) - 1
    
    for i, n in enumerate(name):
        answer += min(ord(n)-ord('A'), ord('Z')-ord(n)+1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) -next)])
        
    answer += min_move
    
    return answer

name = "JEROEN"
print(solution(name))


# 다른 사람 풀이
def solution(name):
    m = [ min(ord(c) - 65, 91-ord(c)) for c in name]       

    answer = 0
    where = 0

    while True:    
        answer += m[where]
        m[where] = 0

        if sum(m) == 0:
            break

        left, right = (1,1)

        while m[where - left] <= 0:
            left += 1
        while m[where + right] <= 0:
            right += 1

        answer += left if left < right else right
        where += -left if left < right else right

    return answer