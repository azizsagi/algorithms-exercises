# Coding exercise
# Browser history with Forward and Back 
# Using STACK Append and POP - LIFO approach 

def browser_history(operations:int, history:str = []):
    
    temp_history = []
    i = 0
    history_path = "/home"
    
    while i < operations:
         if history[i] == "forward":
             if history[i] != "back" and history[i] !="forward":
                temp_history.append(history[i+1])
             i = i + 2
         elif history[i] == "back":
             temp_history.pop()
             i = i + 1
         else:
            if history[i] != "back" and history[i] !="forward":
               temp_history.append(history[i])
            i = i + 1

    for path in temp_history:
        history_path = history_path + "/" + path
    
    return history_path

    
   


#Test
operations = 7
history = ["profiles", "users", "forward", "back", "access", "check", "back" ]
print(browser_history(operations,history))
