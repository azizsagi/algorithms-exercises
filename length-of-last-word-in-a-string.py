# Coding exercise
# Length of last word in a string

given_string = "This is a nice way of doing coding "


def count_last_word(given_string):
    refined_string = given_string.strip().split()         #trim and split with spaces
    return len(refined_string[len(refined_string)-1])     #get the length for the last string in splitted array


print(count_last_word(given_string))