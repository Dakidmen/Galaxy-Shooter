import curses;

#iniate screen
screen = curses.initscr()
weight, height = screen.getmaxyx();
curses.curs_set(0);
sh, sw = screen.getmaxyx();
w = curses.newwin(sh, sw, 0,0);
w.keypad(1);

w.timeout(1);
