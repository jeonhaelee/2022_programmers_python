from itertools import permutations


def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_count(sub_nums, i):
    count = 0
    sub_stack = []
    for n in sub_nums:
        if int(n[0]) == 0:
            continue
        word = ''.join(n)
        number = int(word)
        if number in sub_stack:
            continue
        else: 
            sub_stack.append(number)
            if is_prime(number):
                count += 1
    print("sub_stack : {}".format(sub_stack))
    print("count : {}".format(count))
    return count
    
def solution(numbers):
    answer = 0
    
    nums = []
    for i in range(len(numbers)):
        nums.append(numbers[i])
    print("nums : {}".format(nums))
    
    stack = []
    for i in range(len(nums)):
        if nums[i] in stack:
            continue
        else:
            if is_prime(int(nums[i])):
                stack.append(nums[i])
                answer += 1
    print("1개씩 소수 확인 후 answer : {}".format(answer))
    
    for i in range(2, len(nums)+1):
        sub_nums = list(permutations(nums, i))
        print("{}개씩 sub_nums : {}".format(i, sub_nums))
        answer += prime_count(sub_nums, i)
        
    return answer

numbers = "17"
print(solution(numbers))