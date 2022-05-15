from audioop import reverse


def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    while len(A) > 0:
        answer += (A[0]*B[0])
        del A[0]
        del B[0]
    return answer

A = [1, 4, 2]
B = [5, 4, 4]	
print(solution(A,B))