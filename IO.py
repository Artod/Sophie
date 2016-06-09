import time
import curses
import atexit

def cleanup():
   curses.nocbreak()
   curses.echo()
   curses.endwin()

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
atexit.register(cleanup)


stdscr.nodelay(1)

while True:

   stdscr.clear()
   for i in xrange(0,5):
    stdscr.addstr("Sophie >> \n")
    stdscr.addstr("Me >> \n")
   time.sleep(0.1)
   c = stdscr.getch()

   if c == curses.'a':
    stdscr.addstr("Sophie >> \n")
   elif c == curses.'b':
    stdscr.addstr("Me >> \n")
   elif c != curses.ERR:
      break
      
class Screen:
    def eventloop():
          pass
    
    
    
def main():
    screen = Screen()
    screen.eventloop()
# IO elements
# Label - Text printing
# Textbox - User can enter into this
# Passbox - Password box
# Listbox - Choose from list of options, add extra options
# Checkbox - Choose one or more options from a list of options
# Graph - Plot simple 2D Graphs
# Button - Pressable button
# Panel - Arrange widgets and address them in a hierarchical fashion
# Table - Print in a well formatted table
# Screen - Describe the state of the screen currently

# Basically ncurses updates the screen whenever a state changed event occurs on any of the children widgets
# and it is passed upwards and reaches screen
# It does not unnecessarily update everything
# We need to think of someway of implementing callbacks
