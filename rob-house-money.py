# Given a row with money stored in a particular house
# Rob the max amount of money
# can rob as many houses as we want but we can't rob the two adjacant houses as it will trigger the police
# Example: [5,11,4,3] Max will be second home + 4th home = 11 + 3 = 14 the max we can rob 


#Method 1
def rob_home(homes):
    l = len(homes)  # The length of the given homes

    if l==1: return homes[0]
    if l==2: return max(homes)

    maxx = [homes[0], max(homes[0], homes[1])]

    for i in range(2, l):
        curr = max(homes[i] + maxx[i-2], maxx[i-1])
        maxx.append(curr)

    return maxx[-1]


#Method 2

def rob_homes_2(nums) -> int:        
        r1 = 0
        r2 = 0
        for i in nums:
            temp = max(i+r1,r2)
            r1 = r2
            r2 = temp
        return r2
# Test cases

print(rob_homes_2([5,10,5,4])) #Output = 14
#print(rob_home([1, 2, 3, 4, 5, 6, 7]))  #Output = 16




