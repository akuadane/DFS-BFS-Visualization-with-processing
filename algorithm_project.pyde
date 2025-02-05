from functions import *



n=20
goal = (n-1,n-1)
puzzle = create_maze(n)
solver_func = solve_puzzle_dfs
path,explored= solver_func(puzzle,goal,(0,0))
not_with_mem = True

# constants
bs=30
bh=30
h= n*bs+bh
w = n*bs
speed= 5

# varibables that change
cur = 1
frame = 0
play_explored = True

clicked = False
bt=["Depth first","Depth first with mem","Breadth first","Change maze"]

def setup():
    
    size(w,h)
    rectMode(CORNER)
    textSize(16)
    textAlign(CENTER)
    
    
def draw():
    global frame,cur,play_explored
    background(255)
    
    # draw the buttons
    stroke(255)
    
    for i in range(4):
        fill(0,0,255)
        rect(w/4*i,0,w/4,bh)
        fill(255)
        text(bt[i],w/4*i + w/8,bh/1.5)
    
    # draw the puzzle
    for r in range(n):
        for c in range(n):
            v = puzzle[r][c]
            stroke(255*v)
            fill(255*v)
            
            rect(c*bs,r*bs+bh,bs,bs)
    # draw the end goal
    stroke(0,255,0)
    fill(0,255,0)
    rect(goal[0]*bs,goal[1]*bs+bh,bs,bs)
    
    to_be_drawn=[]
    rd,g,b = 100,100,200
    if not play_explored:
        to_be_drawn = path
        rd,g,b= 100,200,100
    else:
        to_be_drawn = explored
    
        
    for i in range(cur):
        if i< len(to_be_drawn):
            r,c = to_be_drawn[i]
            stroke(rd,g,b)
            fill(rd,g,b)
            rect(c*bs,r*bs+bh,bs,bs)        
    
    
    frame+=1
    if frame==speed:
        frame=0
        cur+=1
        if cur>len(to_be_drawn):
            play_explored = not play_explored
            cur=0
        
    # paint the head of the explorer a different color
    stroke(255,0,0)
    fill(255,0,0)
    rect(c*bs,r*bs+bh,bs,bs)


def mouseClicked(event):
    global path,explored,cur,frame,play_explored,puzzle,solver_func,n,not_with_mem 

    if event.y < bh:
        if event.x < w/4:
            solver_func = solve_puzzle_dfs
            not_with_mem = True
        elif event.x < w/4 * 2:
            solver_func = solve_puzzle_dfs_mem
            not_with_mem = False
        elif event.x < w/4 * 3:
            solver_func = solve_puzzle_bfs
            not_with_mem = True
        else:
            puzzle = create_maze(n)
            
        if not_with_mem:
            path,explored= solver_func(puzzle,goal,(0,0))
        else:
            mem = [[0]* n for _ in range(n)]
            path,explored = solver_func(puzzle,goal,mem,(0,0))
            
            
        cur = 1
        frame = 0
        play_explored = True
