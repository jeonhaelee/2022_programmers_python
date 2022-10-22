# 가장 큰  수


from functools import cmp_to_key

def compare(str1, str2):
    sen1 = int(str1 + str2)
    sen2 = int(str2 + str1)
    if sen1 > sen2:
        return -1
    elif sen1 < sen2:
        return 1
    else: return 0
    
def solution(numbers):
    answer = ''
    n_sort = sorted((map(str, numbers)), key=cmp_to_key(compare))
    
    for n in n_sort:
        answer += n
        
    answer = int(answer)
    
    return str(answer)