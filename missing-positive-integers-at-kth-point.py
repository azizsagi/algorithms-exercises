# two inputs
# Find missing positive integers as Kth point

nums = [2,3,4,7,11] #input
k = 3  #input
positive_number = 1
missing_nums = [] # Range from 1 to 1000

while positive_number <= 1000:
    if positive_number not in nums:
        missing_nums.append(positive_number)
    positive_number = positive_number + 1

print("Missing number is ", missing_nums[k-1])