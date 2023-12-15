# Coding exercise
# Check if contains duplicates

def check_duplicates(nums):
    set_num = list()  # using empty list
    for item in nums:
        if item in set_num:
            return True
        else:
            set_num.append(item)

    return False


#Test
items = [1, 2, 5, 6, 7, 9]
print(check_duplicates(items))
