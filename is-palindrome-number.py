# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.
# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

def isPalindrome(x: int) -> bool:
        s = str(x)
        left = 0
        right = len(s)-1

        for i in range(len(s)):
            if s[left] != s[right]:
                return False
            left +=1
            right -= 1

        return True

#without converting to string
def isPalindromeSecond(x: int) -> bool:
         if x < 0:
            return False
         reversed_num = 0
         temp = x

         while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

         return reversed_num == x

print(isPalindromeSecond(121))