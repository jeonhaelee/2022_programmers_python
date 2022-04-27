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
    for n in sub_nums:
        word = ""
        for i in range(i):
            word += n[i]
        number = int(word)
        if is_prime(number):
            count += 1
    return count
    
def solution(numbers):
    answer = 0
    nums = []
    for i in range(len(numbers)):
        nums.append(numbers[i])
    print("nums : {}".format(nums))
    for i in range(1, len(nums)+1):
        sub_nums = permutations(nums, i)
        print("sub_nums : {}".format(sub_nums))
        answer += prime_count(sub_nums, i)
    return answer

numbers = "17"
print(solution(numbers))