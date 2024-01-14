# Follow the steps below to solve the problem:

# Traverse the array, Ignore the elements which are greater than N and less than 1.
# While traversing, check if a[i] ? a[a[i]-1] holds true or not .
# If the above condition is true then swap a[i] and a[a[i] – 1]  and swap until (a[i] ? a[a[i] – 1]) condition fails.
# Traverse the array and check whether a[i] ? i + 1 then return i + 1.
# If all are equal to its index then return N+1.


# Python program for the above approach
 
 
# Function for finding the first
# missing positive number
def firstMissingPositive(arr, n):
 
    # Loop to traverse the whole array
    for i in range(n):
 
        # Loop to check boundary
        # condition and for swapping
        while (arr[i] >= 1 and arr[i] <= n
               and arr[i] != arr[arr[i] - 1]):
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
 
    # Checking any element which
    # is not equal to i + 1
    for i in range(n):
        if (arr[i] != i + 1):
            return i + 1
 
    # Nothing is present return last index
    return n + 1
 
 
# Driver code
if __name__ == '__main__':
    arr = [1,2,3,5,7,200,256,25666]
    n = len(arr)
    ans = firstMissingPositive(arr, n)
    print(ans)