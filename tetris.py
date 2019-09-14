'''
Created on 2013. 7. 4.

@author: CHOIMUNSUK,BDS,KYW
'''

import pygame
from pygame.locals import *
pygame.init()
disp=pygame.display.set_mode((250,500))

#block -> block_temp : need check
def cpy_block(stage_temp, block_temp, x, y):
    for i in range(4):
        for j in range(4):
            if block_temp[i][j]==1:
                stage_temp[i+y][j+x]=block_temp[i][j]

#rotation : need check
def rotation(block_temp):
    d=0
    block_temp_r=copy.deepcopy(block_temp)
    for i in range(4):
        for j in range(4):
            block_temp_r[i][j]=block_temp[3-j][i]
    for i in range(4):
        for j in range(4):            
            if block_temp_r[i][j]==1 and 1==stage[y+i][x+j]:
                d=1

    if d==0:
        return copy.deepcopy(block_temp_r)
    if d==1:
        for i in range(4):
            for j in range(4):
                block_temp_r[i][j]=block_temp[j][3-i]
        for i in range(4):
            for j in range(4):            
                if block_temp_r[i][j]==1 and 1==stage[y+i][x+j]:
                    d=2
                else:
                    return copy.deepcopy(block_temp_r)
    if d==2:
        return block_temp   



import sys
import random
import copy
img=pygame.image.load("suji.png")
intro=pygame.image.load("intro.png")
game_over=pygame.image.load("game_over.png")
clock = pygame.time.Clock()
tick = 0
FPS = 45

xxx2=0


def init():
    global stage, stage_temp, block, block_temp, block_temp_r, stage_shadow

    stage = [[1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    stage_temp= [[1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    stage_shadow = [[1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    block = [[[0,0,0,0],
              [1,1,1,1],
              [0,0,0,0],
              [0,0,0,0]],
             [[0,0,0,0],
              [0,1,1,0],
              [0,1,1,0],
              [0,0,0,0]],
             [[0,0,0,0],
              [0,0,1,0],
              [0,1,1,1],
              [0,0,0,0]],
             [[0,0,0,0],
              [0,1,0,0],
              [0,1,1,0],
              [0,0,1,0]],
             [[0,0,0,0],
              [0,0,1,0],
              [0,1,1,0],
              [0,1,0,0]],
             [[0,0,0,0],
              [0,1,0,0],
              [0,1,0,0],
              [0,1,1,0]],
             [[0,0,0,0],
              [0,0,1,0],
              [0,0,1,0],
              [0,1,1,0]]]
    
    block_temp=[[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]  
    block_temp_r=[[0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0]]
init()

#intro
disp.blit(intro,(0,0))
pygame.display.update()
while True:
    flag=0
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            flag=1
    if flag==1:
        break

while True:
    xxx=0
    xxx3=0            
 
    x=4
    y=0
    c=0
    flag = 0    
    if c==0:
        n=random.randint(0,6)
        
    keys=pygame.key.get_pressed()
    if keys[K_x]:
        n=0
    if keys[K_z]:
        n=1

    block_temp=copy.deepcopy(block[n])    
#check gameover
    for i in range(4):
        for j in range(4):
            if block_temp[i][j]==1 and stage[i+y][j+x]==1:
                disp.blit(game_over,(0,0))
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        if event.type==QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type==KEYDOWN:
                            if event.key==K_ESCAPE:
                                flag=1
                                pygame.quit()
                                sys.exit()
                            if event.key==K_RETURN:
                                flag=2
                                
                    if flag==1 or flag==2:
                        break
    if flag==1:
        break
    if flag==2:
        init()
        continue   
                
#erase lines
    for i in range(1,21):
        if sum(stage[i])==14:
            for j in range(i,0,-1):
                stage[j]=copy.deepcopy(stage[j-1])
    stage[0]=[1,1,0,0,0,0,0,0,0,0,0,0,1,1]
    
#falling part : need check
#block loop
    while c==0:
        tick = tick + 1
        d=0
        stage_temp=copy.deepcopy(stage)
        cpy_block(stage_temp, block_temp, x, y)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        
        keys=pygame.key.get_pressed()

        if tick%60==0 or keys[K_DOWN]:
            d=1
            for i in range(4):
                for j in range(4):
                    if stage[y+i+1][x+j]==1 and block_temp[i][j]==1:
                        c=1
                        d=0
            if d==1:
                y=y+1
            
                                             
#get input : need check
        if keys[K_RIGHT] and xxx==0:
            xxx=tick
            d=1
            for i in range(4):
                for j in range(4):
                    if x+j+1<len(stage[y+i]):
                        if stage[y+i][x+j+1]==1 and block_temp[i][j]==1:
                            d=0
            if d==1:
                x=x+1
        if keys[K_LEFT] and xxx==0:
            xxx=tick
            d=1
            for i in range(4):
                for j in range(4):
                    if stage[y+i][x+j-1]==1 and block_temp[i][j]==1:
                        d=0
            if d==1:
                x=x-1
        if keys[K_UP] and xxx3==0:
            xxx3=tick
            block_temp = rotation(block_temp)
            
        if keys[K_SPACE] and xxx2==0:
            xxx2=tick
            d=1
            while d==1:
                for i in range(4):
                    for j in range(4):
                        if stage[y+i+1][x+j]==1 and block_temp[i][j]==1:
                            d=0
                if d==1:
                    y=y+1
                else:
                    c=1
                    stage_temp=copy.deepcopy(stage)
                    cpy_block(stage_temp, block_temp, x, y)
            
                             
        if (tick-xxx) > 5 :
            xxx=0
        if (tick-xxx2) > 5 :
            xxx2=0
        if (tick-xxx3) > 5 :
            xxx3=0
#display part
        clock.tick(FPS)
        disp.blit(img,(0,0))
        for i in range(1,21):
            for j in range(2,12):
                if stage_temp[i][j]==1:
#                    pygame.draw.rect( disp, (255, 255, 255), ((j-2)*25,(i-1)*25,25,25) ) 
                    rect = pygame.Surface((25,25), pygame.SRCALPHA, 32)
                    rect.fill((255, 128, 128, 75))
                    disp.blit(rect, ((j-2)*25,(i-1)*25))
                    pygame.draw.rect( disp, (0, 0, 0), ((j-2)*25,(i-1)*25,25,25),1)
                
        pygame.display.update()


#copy part        
        if c==1:
            for i in range(2,22):
                for j in range(2,12):
                    if stage_temp[i][j]==1:
                        stage[i][j]=stage_temp[i][j]
            break