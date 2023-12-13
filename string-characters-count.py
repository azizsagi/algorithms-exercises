# Coding exercise
# Count string characters

testing_string = "Muhammed Faruk Aziz"

# Logic - Everything in Python is an object. :)


def count_characters(given_string):
    obj = {}
    for ch in given_string:
        if ch in obj:
            obj[ch] += 1
        else:
            obj[ch] = 1

    return obj


print(count_characters(testing_string))
