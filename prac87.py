# H-Index


from bisect import bisect_left

def solution(citations):
    answer = 0
    citations.sort()
    
    for h in range(len(citations)+1):
        if h <= len(citations[bisect_left(citations, h):]):
            answer = max(answer, h)
        
    return answer