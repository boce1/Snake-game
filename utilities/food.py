import pygame
from utilities.parameters import food_img, HEIGHT, WIDTH

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = food_img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.positions = [(x, y) for x in range(0, WIDTH - self.width + 1, self.width) 
        for y in range(0, HEIGHT - self.height + 1, self.height)]

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))