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
