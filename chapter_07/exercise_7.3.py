# The function eval_loop iteratively prompts the user for input,
# evaluates the input using the build-in eval funciton, and prints 
# the result.
def eval_loop():
    line = raw_input('Please enter an expression to evaluate, or done to exit\n')
    while True:
        if line == 'done':
            break
        print eval(line)
        line = raw_input('Please enter an expression to evaluate, or done to exit\n')
 
eval_loop()