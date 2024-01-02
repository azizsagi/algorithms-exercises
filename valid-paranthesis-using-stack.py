# Coding exercise
# Check if given paranthesis are valid. 
# Example: [{()}] is valid as opening and closing both are there while [{](}] not valid

def is_valid_paran(s: str):

    #Crate an empty list as a stack
    stack = []

    #create a dict with closing and open paranthesis
    close_to_open = {")":"(","}":"{","]":"["}

    #going through loops
    for char in s:
        if char in close_to_open:
            if not stack: return False
            top_element = stack.pop()
            if close_to_open[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack


#Examples
print(is_valid_paran("[{()}]"))
print(is_valid_paran("[{}]"))
print(is_valid_paran("[{()}"))
print(is_valid_paran("[{(}]"))
print(is_valid_paran("[{("))