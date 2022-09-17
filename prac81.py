# 주차 요금 계산
# 기본시간, 기본요금, 단위시간, 단위요금


from datetime import datetime


## 누적시간에 따른 요금계산 함수 만들기
def cal_cash(dic):
    
    
    
    
def solution(fees, records):
    answer = []
    car_li = []; time_li = []
    dic = {}
    
    for record in records:
        
        car_num = record[6:10]
        if car_num not in dic:
            dic[car_num] = datetime.strptime('00:00', '%H:%M')
            
        if record[11:] == "IN": # in 일 때
            if car_num not in car_li:
                car_li.append(car_num)
                d = datetime.strptime(record[:5], '%H:%M')
                time_li.append(d)
                
        else: # out 일 때
            idx = car_li.index(car_num)
            d = datetime.strptime(record[:5], '%H:%M') - time_li[idx]
            print(f'd : {d}')
            dic[car_num] += d
            del car_li[idx]
            del time_li[idx]
            
    dic.sort()
    
    ## car_li에 남아있는 아직 out 하지 않은 자동차 시간도 따져서 더해주기
    
    
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
           "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))