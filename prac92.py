# 이모티콘 할인행사


from itertools import product

def solution(users, emoticons):
    people = 0 # 이모티콘 플러스 서비스 가입자 수 <- 1순위
    money = 0 # 이모티콘 매출액 <- 2순위
    
    percent = [10, 20, 30, 40] # 할인율 종류 리스트
    percent_li = list(product(percent, repeat=len(emoticons))) # 중복 순열을 이용하여 이모티콘별 할인율 리스트 만들기
    
    for case in percent_li: # case별로 하나씩 확인하며 업데이트
        tmp_people = 0 # case에 해당하는 이모티콘 플러스 서비스 가입자 수
        tmp_money = 0 # case에 해당하는 이모티콘 매출액
        
        for user in users: 
            emo_price = 0 # 해당 유저의 이모티콘 가격
            
            for idx in range(len(emoticons)): # 이모티콘을 돌며 하나씩 확인
                if case[idx] >= user[0]: # 유저의 할인 기준보다 할인율이 더 클 경우만 이모티콘 구입
                    new_price = emoticons[idx] * (100 - case[idx]) / 100 # 할인이 적용된 이모티콘 가격
                    emo_price += new_price 
        
            if emo_price >= user[1]: # 유저의 가격 기준보다 지불해야 할 가격이 더 클 경우 서비스 가입
                tmp_people += 1
            else:
                tmp_money += emo_price
                
        # 서비스 가입자 수와 매출액을 비교하며 계속해서 업데이트
        if tmp_people > people:
            people = tmp_people
            money = tmp_money
        elif tmp_people == people:
            if tmp_money >= money:
                money = tmp_money

    return [people, int(money)]

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]

print(solution(users, emoticons))