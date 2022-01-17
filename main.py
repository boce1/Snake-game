from turtle import window_width
import pygame
from random import choice
from utilities import * 
pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

pygame.font.init()
font = pygame.font.SysFont("Consolas", 50)
main_screne_mess = font.render("Press anything to start", True, WHITE)

s = Snake(0, 0)
f = Food(500, 500)

bg_y = 0
up = True
def background(win):
    global bg_y, up
    speed = 2
    win.blit(background_img, (0, bg_y))
    if up:
        bg_y -= speed
    if bg_y <= -HEIGHT:
        up = False
    if not up:
        bg_y += speed
    if bg_y >= 0:
        up = True

menu = True
ms_mes_x = WIDTH // 2 - main_screne_mess.get_width() // 2
ms_mes_y = HEIGHT // 2 - main_screne_mess.get_height() // 2
top_y = ms_mes_y - main_screne_mess.get_height() // 2
bottom_y = ms_mes_y + main_screne_mess.get_height() // 2
ms_up = True
def main_menu(win):
    global run, menu, ms_mes_y, ms_up
    speed = 2
    while menu or s.menu:
        clock.tick(FPS)
        win.blit(background_img, (0, 0))
        win.blit(main_screne_mess, (ms_mes_x, ms_mes_y))
        if ms_up:
            ms_mes_y -= speed
        if ms_mes_y <= top_y:
            ms_up = False
        if not ms_up:
            ms_mes_y += speed
        if ms_mes_y >= bottom_y:
            ms_up = True
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                menu = False
                s.menu = False
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                menu = False
                s.menu = False
        continue
    
eating_sound = pygame.mixer.Sound("sounds\\eating.wav")
def snake_eat_peach():
    if s.x == f.x and s.y == f.y:
        possible_cor = []
        for cor in f.positions:
            if cor not in s.tail:
                possible_cor.append(cor)
        pygame.mixer.Sound.play(eating_sound)
        f.x, f.y = choice(possible_cor)
        s.tail_len += 1 

pygame.mixer.music.load("sounds\\ShootingStar.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    background(window)
    main_menu(window)
    snake_eat_peach()
    f.draw(window)
    s.draw(window)
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        s.change_direction(event)

pygame.quit()