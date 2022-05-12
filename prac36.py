
def count_num(h, citations):
    count = 0
    for num in citations:
        if num >= h:
            count += 1
    return count

def solution(citations):
    n = len(citations)
    for h in range(n-1, -1, -1):
        if h == count_num(h, citations):
            return h

citations = [3, 0, 6, 1, 5]
print(solution(citations))

# h는 n보다 작음
# n은 citations의 길이

#어떤 과학자가 발표한 논문 n편 중, 
# h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 
# h의 최댓값이 이 과학자의 H-Index입니다.

# n편 중 h편 이상이 h번 이상 인용되었고, n-h 즉 나머지 논문은 h번 이하 인용됨