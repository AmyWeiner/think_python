# The function do_twice takes two arguments, a function object and a value, 
# and calls the function twice, passing the value as an argument.

def do_twice(func, val):
    func(val)
    func(val)

# The function print_twice takes a string as a parameter and prints it twice.

def print_twice(str):
    print str
    print str

do_twice(print_twice, 'spam')

# The function do_four takes a function object and a value, and calls the function 
# four times, passing the value as a parameter. There are only two statements in 
# the body of this function, not four.

def do_four(func, val):
    do_twice(func, val)
    do_twice(func, val)

do_four(print_twice, 'spam')