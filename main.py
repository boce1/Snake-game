import pygame
from random import choice
from utilities import * 
pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

s = Snake(100, 100)
f = Food(500, 500)

def draw(win):
    win.fill(BLACK)
    f.draw(win)
    s.draw(win)
    pygame.display.update()

def snake_eat_peach():
    if s.x == f.x and s.y == f.y:
        possible_cor = []
        for cor in f.positions:
            if cor not in s.tail:
                possible_cor.append(cor)
        f.x, f.y = choice(possible_cor)
        s.tail_len += 1 

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    snake_eat_peach()
    draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        s.change_direction(event)

pygame.quit()