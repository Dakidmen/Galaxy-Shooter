import curses;
import random;
import time;

#iniate screen
screen = curses.initscr()
weight, height = screen.getmaxyx();
curses.curs_set(0);
sh, sw = screen.getmaxyx();
w = curses.newwin(sh, sw, 0,0);
w.keypad(1);

w.timeout(1);

#Ship body:

ship_x = sw/4;
ship_y = sh/2;

ship = [
    [ship_y, ship_x]
];
wingL = [[int(ship_y), int(ship_x-1)]];
wingR = [[int(ship_y), int(ship_x+1)]];

#Starting cannons:
#   Up
cannon = [[int(ship_y-1), int(ship_x)]];
#   Left
cannonLeft = [[int(ship_y), int(ship_x-2)]];
#   Right
cannonRight = [[int(ship_y), int(ship_x+2)]];

#Starting shooters:
def shoot(y,x,right,left):
    '''shoots cannon, only shoots side cannons after boost is true'''
    leftS = None;
    rightS = None;
    upS = [[int(y-2), int(x)]];
    w.addch(upS[0][0], upS[0][1], '¦');

    if True in right:
        rightS = [[int(y-1), int(x+2)]];
        w.addch(rightS[0][0], rightS[0][1], '¦');
    if True in left:
        leftS = [[int(y-1), int(x-2)]];
        w.addch(leftS[0][0], leftS[0][1], '¦');
    
    return upS;

def shootPosition(y,x):
    y = int(y)
    x = int(x)
    return y,x

#Starting booster:
boostLeft = [sh//2, sw//2];
w.addch(boostLeft[0], boostLeft[1], 'O');
boostRight = [sh//6, sw//6];
w.addch(boostRight[0], boostRight[1], 'X');

key = None;
shootRight = False;
shootLeft = False;
shootUp = False;
shoot = False;
#body = [ship[0],wingL[0],wingR[0],cannonLeft[0],cannonRight[0],cannon[0]];

#Start Game
while True:
    next_key = w.getch();
    key = key if next_key == -1 else next_key;

    #adding more body to ship:
    new_head = [ship[0][0], ship[0][1]];
    new_wingL = [wingL[0][0], wingL[0][1]];
    new_wingR = [wingR[0][0], wingR[0][1]];
    #           x coord       y coord
    new_cannon = [cannon[0][0], cannon[0][1]];
    new_cannonLeft = [cannonLeft[0][0], cannonLeft[0][1]];
    new_cannonRight = [cannonRight[0][0], cannonRight[0][1]];
    #Bullets:
    bulletUp = [[int(new_head[0]-2), int(new_head[1])]];
    new_bulletUp = [bulletUp[0][0], bulletUp[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1;
        new_cannonLeft[0] += 1
        new_cannonRight[0] += 1
        new_cannon[0] += 1
        new_wingL[0] += 1
        new_wingR[0] += 1
        key = None;
    if key == curses.KEY_UP:
        new_head[0] -= 1;
        new_cannonLeft[0] -= 1
        new_cannonRight[0] -= 1
        new_cannon[0] -= 1
        new_wingL[0] -= 1;
        new_wingR[0] -= 1
        key = None;
    if key == curses.KEY_LEFT:
        new_head[1] -= 1;
        new_cannonLeft[1] -= 1
        new_cannonRight[1] -= 1
        new_cannon[1] -= 1
        new_wingR[1] -= 1;
        new_wingL[1] -= 1
        key = None;
    if key == curses.KEY_RIGHT:
        new_head[1] += 1;
        new_cannonLeft[1] += 1
        new_cannonRight[1] += 1
        new_cannon[1] += 1
        new_wingL[1] += 1
        new_wingR[1] += 1
        key = None;

    #SHOOT !
    if key == curses.KEY_HOME:
        shoot = True;
        current_y, current_x = shootPosition(new_head[0],new_head[1]);
        # bulletUp = shoot(new_head[0],new_head[1],shootRight,shootLeft);
        for z in range(current_y,0,-1):
            screen.clear()
            screen.addch(z,current_x, '¦');
            screen.refresh();
            time.sleep(0.2)
        key = None;
        
    ship.insert(0,new_head);
    wingL.insert(0,new_wingL);
    wingR.insert(0,new_wingR);
    cannon.insert(0,new_cannon);
    cannonLeft.insert(0,new_cannonLeft);
    cannonRight.insert(0,new_cannonRight);
    if shoot == True:
        bulletUp.insert(0, new_bulletUp);
    
    

    
    #if ship gets boostLeft:
    if (ship[0] == boostLeft) or (cannonLeft[0] == boostLeft) or (cannonRight[0] == boostLeft) or (cannon[0] == boostLeft):
        boostLeft = None;
        while boostLeft is None:
            new_boostLeft = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            boostLeft = new_boostLeft if new_boostLeft not in ship else None;
        w.addch(boostLeft[0], boostLeft[1], 'O');
        shootLeft = True;
    #if ship gets boostRight:
    if (ship[0] == boostRight) or (cannonLeft[0] == boostRight) or (cannonRight[0] == boostRight) or (cannon[0] == boostRight):
        boostRight = None;
        while boostRight is None:
            new_boostRight = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            boostRight = new_boostRight if new_boostRight not in ship else None;
        w.addch(boostRight[0], boostRight[1], 'X');
        shootRight = True;
    else:
        #Movement allow of:
        #ship and wings
        tail = ship.pop();
        w.addch(int(tail[0]), int(tail[1]), ' ');
        tailL = wingL.pop();
        w.addch(int(tailL[0]), int(tailL[1]), ' ');
        tailR = wingR.pop();
        w.addch(int(tailR[0]), int(tailR[1]), ' ');
        
        #cannonUp
        tailUp = cannon.pop();
        w.addch(tailUp[0], tailUp[1], ' ');

        #cannonLeft
        tailLeft = cannonLeft.pop();
        w.addch(tailLeft[0], tailLeft[1], ' ');

        #cannonRight
        tailRight = cannonRight.pop();
        w.addch(tailRight[0], tailRight[1], ' ');

        #Bullets
        if shoot == True:
            tailBUp = bulletUp.pop();
            w.addch(tailBUp[0], tailBUp[1], ' ');

    
    w.addch(int(ship[0][0]), int(ship[0][1]), curses.ACS_CKBOARD);
    w.addch(int(wingL[0][0]), int(wingL[0][1]), 'm');
    w.addch(int(wingR[0][0]), int(wingR[0][1]), 'm');
    w.addch(int(cannonLeft[0][0]), int(cannonLeft[0][1]), '‡');
    w.addch(int(cannonRight[0][0]), int(cannonRight[0][1]), '‡');
    w.addch(int(cannon[0][0]), int(cannon[0][1]), 'Ѧ');

    if shoot == True:
        w.addch(int(bulletUp[0][0]), int(bulletUp[0][1]), '¦');
        shoot = False;
