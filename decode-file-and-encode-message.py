def decode_file(message_file):
    """
    I need a function called decode(message_file) that can read in an encoded message from a .txt file and return the decoded version as a string.

    Here's an example of what the message_file .txt file will look like:

    3 love

    6 computers

    2 dogs

    4 cats

    1 I

    5 you

    Raises:
    - FileNotFoundError:
        If the specified file does not exist.
    """

    try:
        # Open the file in read mode
        with open(message_file, 'r') as file:
            # Read all lines from the file
            file_lines = file.readlines()

            # Create an empty list to store the words in the pyramid
            file_words = {}
            decoded_string = ""

            # Iterate over each line in the read file
            for line in file_lines:
                # Split the line from file into number and words
                number, word = line.split()

                # Append the word to the list 'file_words'
                file_words[int(number)] = word
            # Sort the words list in ascending order
            # file_words.sort()

            # Create a list to store the lines of the pyramid
            pyramid = {}
            number = 1
            file_words = dict(sorted(file_words.items()))
           
            # Iterate over each line in the pyramid
            for i in range(1,len(file_words) + 1):
                if number > 1:
                    pyramid[number-1] = file_words[number-1]
                if number <= len(file_words):
                    for j in range(1, i+1):
                        number += 1                    
                else:
                    break
 
            # Join the lines of the pyramid with newline characters and move on
            for key in  pyramid:       
                decoded_string += " "+pyramid[key]

            # Return the decoded message now
            return decoded_string

    except FileNotFoundError:
        raise FileNotFoundError("File not found error")

# Example usage:
message_file = "coding_qual_input.txt"
decoded_message_from_file = decode_file(message_file)
print(decoded_message_from_file)