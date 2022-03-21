import time
import random
import pygame
from generate_emap_lib import generateEmap
import subprocess

pygame.init()
screen = pygame.display.set_mode([800, 800])

lineColor = (0,0,255)
tileColor1 = (99,0,0)
tileColor2 = (0,99,0)
tileColor3 = (0,99,99)

width=10
height=10
grid = [False] * (width*height) # this stores if a tile was visited.

tile_width=40
tile_height=40

wall_height=10

h_lines = [True] * ((width+1)*(height+1))
v_lines = [True] * ((width+1)*(height+1))

stack=[]
stack.append({'x':0,'y':0})

def setVisited(x,y):
    grid[y*height+x]=True

setVisited(0,0)

lastTime = 0

def getUnvisitedNeighbors(pos):
  unvisitedNeighbors = []
  if (pos['x']>0 and not grid[pos['y']*height+pos['x']-1]):
    unvisitedNeighbors.append({'x':pos['x']-1,'y':pos['y'],'dir':'left'})
  if (pos['x']<(width-1) and not grid[pos['y']*height+pos['x']+1]):
    unvisitedNeighbors.append({'x':pos['x']+1,'y':pos['y'],'dir':'right'})
  if (pos['y']>0 and not grid[(pos['y']-1)*height+pos['x']]):
    unvisitedNeighbors.append({'x':pos['x'],'y':pos['y']-1,'dir':'up'})
  if (pos['y']<(height-1) and not grid[(pos['y']+1)*height+pos['x']]):
    unvisitedNeighbors.append({'x':pos['x'],'y':pos['y']+1,'dir':'down'})
  return unvisitedNeighbors


def removeWall(x,y,dir):
  if(dir=='up'):
    h_lines[y*height+x]=False
  if(dir=='down'):
    h_lines[(y+1)*height+x]=False
  if(dir=='left'):
    v_lines[y*height+x]=False
  if(dir=='right'):
    v_lines[y*height+x+1]=False

def createMaze():
  if len(stack)==0:
    return
  cur = stack[-1]
  un = getUnvisitedNeighbors(cur)
  if len(un)==0:
    return stack.pop()
  n = un[random.randint(0,len(un)-1)]
  setVisited(n['x'],n['y'])
  removeWall(cur['x'],cur['y'], n['dir'])
  stack.append(n)

def drawLine(x,y,x2,y2):
    pygame.draw.line(screen,lineColor,(x*tile_width,y*tile_height),(x2*tile_width,y2*tile_height))

def drawLines():
    for x in range(width+1):
        for y in range(height+1):
            if(h_lines[y*height+x]):
                drawLine(x,y,x+1,y)
            if(v_lines[y*height+x]):
                drawLine(x,y,x,y+1)

def drawTiles():
    for x in range(width):
        for y in range(height):
            if(grid[y*height+x]):
                pygame.draw.rect(screen,tileColor1,(x*tile_width, y*tile_height, tile_width, tile_height))
            else:
                pygame.draw.rect(screen,tileColor2,(x*tile_width, y*tile_height, tile_width, tile_height))

def drawCurrentTile():
  if len(stack)>0:
    cur = stack[-1]
    pygame.draw.rect(screen,tileColor3,(cur['x']*tile_width, cur['y']*tile_height, tile_width, tile_height))


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                print("Left mouse button clicked at: ", pos)
                emap = generateEmap(width, height, h_lines, v_lines, 10 ,10 , 10)
                emap.writeMap("C:\\Users\\Ray\\AppData\\LocalLow\\BoundingBoxSoftware\\Prodeus\\LocalData\\Maps\\aaa.emap")
            if pygame.mouse.get_pressed()[2]:
                print("Right mouse button clicked at: ", pos)
                subprocess.run(['D:\\Action\\Steam\\steamapps\\common\\Prodeus\\Prodeus.exe'])

            
    screen.fill((0, 0, 0))

    ct = time.time()
    if(ct>lastTime):
        lastTime = ct+0.01
        createMaze()

    drawTiles()
    drawCurrentTile()
    drawLines()
    pygame.display.flip()

pygame.quit()

