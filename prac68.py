# 수식 최대화

# 내 풀이

from itertools import permutations
import copy

def do_minus(numbers_2, cal_2):
    result = 0
    while '-' in cal_2:
        idx = cal_2.index('-')
        result = numbers_2[idx]
        result -= numbers_2[idx+1]
        numbers_2[idx] = result
        del numbers_2[idx+1]
        del cal_2[idx]

def do_plus(numbers_2, cal_2):
    result = 0
    while '+' in cal_2:
        idx = cal_2.index('+')
        result = numbers_2[idx]
        result += numbers_2[idx+1]
        numbers_2[idx] = result
        del numbers_2[idx+1]
        del cal_2[idx]
        
def do_multi(numbers_2, cal_2):
    result = 0
    while '*' in cal_2:
        idx = cal_2.index('*')
        result = numbers_2[idx]
        result *= numbers_2[idx+1]
        numbers_2[idx] = result
        del numbers_2[idx+1]
        del cal_2[idx]



def solution(expression):

    numbers = []; cal = []
    num = ""
    for i in range(len(expression)):
        if expression[i].isdigit() :
            num += expression[i]
        else:
            cal.append(expression[i])
            numbers.append(int(num))
            num = ""
    numbers.append(int(num))
    
    cals_permutations = []
    cals_permutations.append(list(permutations(set(cal))))

    results = []
    for cals in cals_permutations[0]:

        numbers_2 = copy.deepcopy(numbers)
        cal_2 = copy.deepcopy(cal)

        for a in cals:
            if a == '-':
                do_minus(numbers_2, cal_2)
            elif a == '+':
                do_plus(numbers_2, cal_2)
            elif a == '*':
                do_multi(numbers_2, cal_2)
        
        results.append(abs(numbers_2[0]))

    answer = max(results)
    
    return answer

expression = "50*6-3*2"
print(solution(expression)) #300

# 다른 사람 풀이
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)