import curses;
import random;

#iniate screen
screen = curses.initscr()
weight, height = screen.getmaxyx();
curses.curs_set(0);
sh, sw = screen.getmaxyx();
w = curses.newwin(sh, sw, 0,0);
w.keypad(1);

w.timeout(1);

ship_x = sw/4;
ship_y = sh/2;

ship = [
    [ship_y, ship_x]
];


#Starting cannons:

#   Up
#cannon = [int(ship_y+1), int(ship_x)];
#w.addch(cannon[0], cannon[1], '^');

#   Left
cannonLeft = [[int(ship_y), int(ship_x-1)]];
w.addch(cannonLeft[0][0], cannonLeft[0][1], '^');

#   Right
cannonRight = [[int(ship_y), int(ship_x+1)]];
w.addch(cannonRight[0][0], cannonRight[0][1], '^');

key = None;
while True:
    next_key = w.getch();
    key = key if next_key == -1 else next_key;

    #adding more body to ship:
    new_head = [ship[0][0], ship[0][1]];
    #           x coord       y coord
    new_cannonLeft = [cannonLeft[0][0], cannonLeft[0][1]];
    new_cannonRight = [cannonRight[0][0], cannonRight[0][1]];

    if key == curses.KEY_DOWN:
        new_head[0] += 1;
        new_cannonLeft[0] += 1
        new_cannonRight[0] += 1
        key = None;
    if key == curses.KEY_UP:
        new_head[0] -= 1;
        new_cannonLeft[0] -= 1
        new_cannonRight[0] -= 1
        key = None;
    if key == curses.KEY_LEFT:
        new_head[1] -= 1;
        new_cannonLeft[1] -= 1
        new_cannonRight[1] -= 1
        key = None;
    if key == curses.KEY_RIGHT:
        new_head[1] += 1;
        new_cannonLeft[1] += 1
        new_cannonRight[1] += 1
        key = None;
    
    ship.insert(0,new_head);
    cannonLeft.insert(0,new_cannonLeft);
    cannonRight.insert(0,new_cannonRight);

    '''
    #if ship gets cannonLeft:
    if ship[0] == cannonLeft:
        cannonLeft = None;
        while cannonLeft is None:
            new_cannonLeft = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            cannonLeft = new_cannonLeft if new_cannonLeft not in ship else None;
        w.addch(cannonLeft[0], cannonLeft[1], 'O');
    else:
        tail = ship.pop();
        w.addch(int(tail[0]), int(tail[1]), ' ');
    '''
    #movement allow of:

    #ship
    tail = ship.pop();
    w.addch(int(tail[0]), int(tail[1]), ' ');

    #cannonLeft
    tailLeft = cannonLeft.pop();
    w.addch(tailLeft[0], tailLeft[1], ' ');

    #cannonLeft
    tailRight = cannonRight.pop();
    w.addch(tailRight[0], tailRight[1], ' ');
    
    w.addch(int(ship[0][0]), int(ship[0][1]), curses.ACS_CKBOARD);
    w.addch(int(cannonLeft[0][0]), int(cannonLeft[0][1]), '^');
    w.addch(int(cannonRight[0][0]), int(cannonRight[0][1]), '^');

