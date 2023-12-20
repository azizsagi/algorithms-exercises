# Coding exercise
# Check if the given array is monotonic (increaseing / decreasing contineously)

def check_monotonic(nums):
    increasing = True
    decreasing = True
    index = 0


    while index < (len(nums)-1):
        if nums[index] > nums[index + 1]:
            increasing = False

        if nums[index] < nums[index + 1]:
            decreasing = False

        index += 1

    return increasing or decreasing


# Output
print(check_monotonic([1, 2, 2]))
print(check_monotonic([1, 2, 9,7,5]))
print(check_monotonic([1, 2, 3]))
print(check_monotonic([3, 5, 1]))