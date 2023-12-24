# Coding exercise
# a program that returns the n numbers in a fibonacci sequence for a given range
# Recursion

def fibonacci_of(n:int):
    if n in {0,1}:
        return n
    
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)

#Test case
print([fibonacci_of(n) for n in range (8)])
   
    
    