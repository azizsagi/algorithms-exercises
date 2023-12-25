# Coding exercise
# Number is happy or not. Number is happy if their square root is = 1 else no
# Example - 
# Input = 19
# Output = happy 
# Explaination:
# 1^2  + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1 HAPPY

def isHappy(num:int):
    seen = set()
    cur = str(num)
    while cur not in seen:
        seen.add(cur)
        sum = 0
        for digit in cur: 
            sum += pow(int(digit),2)

        if sum == 1: return True
        cur = str(sum)

    return False

#Test Cases
print(isHappy(201))
print(isHappy(9))
print(isHappy(19))
print(isHappy(1))
print(isHappy(73))
    