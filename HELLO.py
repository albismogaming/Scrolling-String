import time
import string
import sys

def scroll_print(word, delay=0.1):
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    accumulated_output = ""  # String to accumulate the output
    for char in word:
        if char not in alphabet:
            accumulated_output += char  # Add non-alphabet characters directly
        else:
            for letter in alphabet:
                print(accumulated_output + letter, end='\r', flush=True)
                time.sleep(delay)
                if letter.lower() == char.lower():
                    accumulated_output += char  # Add the correct alphabet character
                    break
        time.sleep(delay)  # Short pause after each character
        sys.stdout.flush()

    print(accumulated_output)  # Print the final word

scroll_print("H E L L O")
