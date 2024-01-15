# Coding exercise
# a program that returns the n numbers in a fibonacci sequence for a given range
# Recursion

def fibonacci_of(n:int):
    if n in {0,1}:
        return n
    
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)

def factorial_of(n: int):
    if n == 1:
        return n
    return n * factorial_of(n-1)
    


#Test case
print([fibonacci_of(n) for n in range (8)])
print(factorial_of(5))
   
    
    