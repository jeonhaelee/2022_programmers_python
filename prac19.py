
import heapq as h   # heapq 모듈 import   

def is_scov_all_k(scoville, k):   # scoville에 들어있는 값이 모두 k 이상인지 확인하는 함수
    for i in scoville:
        if i < k:
            return False          # 하나라도 k보다 작으면 False 리턴
    return True                   # 모든 원소가 k보다 크면 True 리턴

def solution(scoville, k):        
    count = 0
    h.heapify(scoville)   # heapify() 함수를 이용해 scoville를 즉각적으로 heap으로 변환시켜줌
    if len(scoville) == 1:                          # scoville의 길이가 1일 때의 조건을 따로 만들어줌
        if is_scov_all_k(scoville, k) == False:     # 왜? 길이가 2 미만이라, 아래 while 문에서 인덱스 오류나므로
            return -1
        else : return 0
    while is_scov_all_k(scoville, k) == False:
        num = h.heappop(scoville)   # heappop() 함수로 scoville에서 가장 작은 원소가 삭제되고 리턴됨
        num += h.heappop(scoville)*2
        h.heappush(scoville,num)    # 위의 계산된 값을 heappush() 함수를 이용해 scoville에 넣어줌
        count += 1
        if len(scoville) == 1:      # while문을 순회하다가도 scoville의 길이가 1이 될 수 있으므로 따로 조건 추가함
            if is_scov_all_k(scoville, k) == False:
                return -1
    return count
