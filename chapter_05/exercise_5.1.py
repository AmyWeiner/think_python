# The function check_fermat takes four integer parameters, a, b, c, and n, 
# and checks to see if Fermat's theorem holds.

def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print 'Holy smokes, Fermat was wrong!'
    else:
        print "No, that doesn't work."

# The function get_input_and_check_fermat prompts the user for input values for
# a, b, c, and, n, converts the input into integers, and uses check_fermat to determine
# whether or not the values violate Fermat's theorem. 
def get_input_and_check_fermat():
    a = int(raw_input("Please enter an integer values for 'a.':\n"))
    b = int(raw_input("Please enter an integer values for 'b.':\n"))
    c = int(raw_input("Please enter an integer values for 'c.':\n"))
    n = int(raw_input("Please enter an integer values for 'n.':\n"))
    check_fermat(a, b, c, n)

get_input_and_check_fermat()