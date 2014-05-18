# The funciton right_justify takes a string, s, as a parameter, and prints the
# string with enough leading spaces so that the last letter of the string is in 
# column 70 of the output display.

def right_justify(s):
    display_width = 70
    string_length = len(s)
    leading_spaces = (70 - string_length) * ' '
    print leading_spaces + s

right_justify('allen')