# 주차요금계산 2

from datetime import timedelta
from datetime import datetime

def car_time(time1, time2):
    time2 = datetime.strptime(time2, '%H:%M').hour * 60 + datetime.strptime(time2, '%H:%M').minute
    time1 = datetime.strptime(time1, '%H:%M').hour * 60 + datetime.strptime(time1, '%H:%M').minute
    return time2 - time1
    
def solution(fees, records):
    answer = []
    base_time, base_fee, unit_time, unit_fee = fees

    info_dic = {} # 차번호 : 들어오거나 나간 시간
    time_dic = {} # 차번호 : 총 주차 시간
    
    # "05:34 5961 IN"
    for record in records:
        time, car, in_out = record.split()
        if car in info_dic:
            if in_out == "IN":
                info_dic[car] = time
            else:
                time_dic[car] += car_time(time, info_dic[car])
                info_dic[car] = time
                
        else:
            info_dic[car] = time
            time_dic[car] = 0
        
    info_dic = dict(sorted(info_dic.items()))
    
    for car in info_dic.keys():
        if time_dic[car] <= 180:
            answer.append(base_fee)
        else:
            result = base_fee + round((time_dic[car] - 180) / unit_time) * unit_fee
            answer.append(result)
        
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))