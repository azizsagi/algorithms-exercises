# Coding exercise
# Given the position of moves
# Determine if the Robots returns to origion which is (0,0)
# Valid Moves only contains  U=Up  L=Left   R=Right   D=Down

def check_origional_position(moves:str):
    x,y = 0,0

    #check the moves
    for move in moves:
        match move:
            case 'U':
                y = y + 1
            case 'D':
                y = y - 1
            case 'L':
                x = x - 1
            case 'R':
                x = x + 1

    
    if x==0 and y == 0:
        return True
    else:
        return False
    

#Test Cases
print(check_origional_position("UD"))
print(check_origional_position("LL"))
print(check_origional_position("UDLR"))
print(check_origional_position("DRUP"))
print(check_origional_position("UP"))
                