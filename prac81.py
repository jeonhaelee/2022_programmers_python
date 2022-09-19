# 주차 요금 계산
# 기본시간, 기본요금, 단위시간, 단위요금

# 내 풀이

from datetime import datetime
from math import ceil


## 누적시간 분으로 변환해주는 함수 만들기
def cal_time(dic):
    
    for c, t in dic.items():
        time = dic[c].hour * 60 + dic[c].minute
        dic[c] = time


## 누적시간에 따른 요금계산 함수 만들기
def cal_cash(fees, dic):
    answer = []
    
    for c, t in dic.items():
        
        if dic[c] <= fees[0]:
            result = fees[1]
            answer.append(result)
            continue
        
        result = fees[1]
        result += ceil((dic[c] - fees[0]) / fees[2]) * fees[3]
        answer.append(result)
    
    return answer
    
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
            dic[car_num] += d

            del car_li[idx]
            del time_li[idx]
            

    ## car_li에 남아있는 아직 out 하지 않은 자동차 시간도 따져서 더해주기
    if len(car_li) > 0:
        for i in range(len(car_li)):
            d = datetime.strptime('23:59', '%H:%M') - time_li[i]
            dic[car_li[i]] += d
            
            
    dic = dict(sorted(dic.items()))
    
    cal_time(dic)
    
    answer = cal_cash(fees, dic)
    
    return answer


# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
#            "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# print(solution(fees, records)) # [14600, 34400, 5000]

# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
# print(solution(fees, records)) # [0, 591]

# fees = [1, 461, 1, 10]
# records = ["00:00 1234 IN"]
# print(solution(fees, records)) # [14841]


# 다른 사람 풀이

from collections import defaultdict
from math import ceil

class Parking:
    def __init__(self, fees):
        self.fees = fees
        self.in_flag = False
        self.in_time = 0
        self.total = 0

    def update(self, t, inout):
        self.in_flag = True if inout=='IN' else False
        if self.in_flag:  self.in_time = str2int(t)
        else:             self.total  += (str2int(t)-self.in_time)

    def calc_fee(self):
        if self.in_flag: self.update('23:59', 'out')
        add_t = self.total - self.fees[0]
        return self.fees[1] + ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1]

def str2int(string):
    return int(string[:2])*60 + int(string[3:])

def solution(fees, records):
    recordsDict = defaultdict(lambda:Parking(fees))
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout)
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]