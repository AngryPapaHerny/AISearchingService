import pygame
import sys
# import numpy as np


WHITE = (255,255,255)
GRAY = (180,180,180)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE =(0,0,255)
BLACK = (0,0,0)

WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH//BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH=15
CROSS_WIDTH = 25

pygame.init() #파이 게임 초기화
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tic Tac Toe AI')
screen.fill(BLACK)

def draw_line(color=WHITE):
    for i in range(1,BOARD_ROWS):
        pygame.draw.line(screen,color,(0,SQUARE_SIZE*i),(WIDTH,SQUARE_SIZE*i),LINE_WIDTH)
        pygame.draw.line(screen,color,(SQUARE_SIZE*i,0),(SQUARE_SIZE*i,HEIGHT),LINE_WIDTH)

draw_line(RED)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            print(pygame.mouse.get_rel())
        
    pygame.display.update()