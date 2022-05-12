def count_num(h, citations):
    count = 0
    for num in citations:
        if num >= h:
            count += 1
    return count

def solution(citations):
    n = len(citations)
    for h in range(n, -1, -1):
        if h <= count_num(h, citations):
            return h
    return 0
