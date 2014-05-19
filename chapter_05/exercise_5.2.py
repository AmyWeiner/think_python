# The function is_triangle takes three integer parameters, a, b, and c, and 
# and prints either 'Yes' or 'No,' depending on whether or not a triangle can
# be formed from lines with the given integer lengths. 
def is_triangle(a, b, c):
    if a + b < c or b + c < a or a + c < b:
          print 'No'
    else:
          print 'Yes'

# The function get_input_and_check_triangle prompts the user for input values for
# a, b, and c, and converts the input into integers, and uses check_triangle to 
# determine whether or not a triangle can be formed from the given values. 
def get_input_and_check_triangle():
    a = int(raw_input("Please enter a positive integer values for 'a.':\n"))
    b = int(raw_input("Please enter a positive integer values for 'b.':\n"))
    c = int(raw_input("Please enter a positive integer values for 'c.':\n"))

    is_triangle(a, b, c)

get_input_and_check_triangle()

