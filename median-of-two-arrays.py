#median of two arrays

nums1 = [1,2]
nums2 = [3,4]

l = nums1 + nums2
l.sort()
n = len(l)

if n % 2 != 0:
    median = n / 2
else:
    a = int(n / 2)
    b = int(a - 1)
    median = (l[int(a)]+l[int(b)]) / 2

print(median)

    
    
