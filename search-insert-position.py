

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

def searchInsert(nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high)

            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                low = mid + 1  # Adjust low pointer
            else:
                high = mid - 1  # Adjust high pointer

        return low  # Return the index for insertion position
        
                

# Drive code
                
print(searchInsert([1,3,5,6],7))