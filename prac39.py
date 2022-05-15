def solution(A,B):
    answer = 0
    while len(A) > 0:
        answer += (min(A)*max(B))
        del min(A)
        del max(B)
    return answer

A = [1, 4, 2]
B = [5, 4, 4]	
print(solution(A,B))