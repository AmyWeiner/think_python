# The function draw_grid prints a two-by-two grid using ASCII characters

def do_four(func):
     func()
     func()
     func()
     func()

def do_twice(func):
  func()
  func()

def draw_top_border():
    print ('+' + ' ' + '- ' * 4) * 2 + '+'

def draw_contents():
    print '|', ' ' * 7, '|', ' ' * 7, '|'

def draw_row():
    draw_top_border()
    do_four(draw_contents)

def draw_grid():
    do_twice(draw_row)
    draw_top_border()

draw_grid()
