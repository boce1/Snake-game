import pygame
from utilities.parameters import HEIGHT, WHITE, WIDTH, snake_img
class Snake:
    def __init__(self, x, y):
        self.img = snake_img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = x
        self.y = y
        self.direction = "right"
        self.speed = 10
        self.tail_len = 1
        self.tail = [(self.x, self.y)]
        self.delay = 75

    def move(self):
        if self.direction == "right":
            #self.x += self.speed
            self.x += self.width
        elif self.direction == "left":
            #self.x -= self.speed
            self.x -= self.width
        elif self.direction == "up":
            #self.y -= self.speed
            self.y -= self.height
        else:
            #self.y += self.speed
            self.y += self.height

    def is_dead(self):
        if (self.x, self.y) in self.tail[0:(len(self.tail) - 1)]:
            self.tail = [(self.x, self.y)]
            self.tail_len = 1

    def track_tail(self):
        if not (self.x < 0 or self.y < 0 or self.x > WIDTH - self.width or self.y > WIDTH - self.width):
            self.tail.append((self.x, self.y))
        if len(self.tail) > self.tail_len:
            self.tail.pop(0)
        #print(self.tail)
        #print(self.tail_len)

    def is_key_pressed(self, key, event):
        if event.type == pygame.KEYDOWN:
            if event.key == key:
                return True
        return False

    def change_direction(self, event):
        if self.is_key_pressed(pygame.K_w, event):
            self.direction = "up"
        if self.is_key_pressed(pygame.K_s, event):
            self.direction = "down"
        if self.is_key_pressed(pygame.K_a, event):
            self.direction = "left"
        if self.is_key_pressed(pygame.K_d, event):
            self.direction = "right"

    def draw(self, win):
        self.move()
        self.track_tail()
        pygame.time.wait(self.delay)
        if self.x >= WIDTH:
            self.x = 0
            self.track_tail()
        if self.x < 0:
            self.x = WIDTH - self.width
            self.track_tail()

        if self.y >= HEIGHT:
            self.y = 0
            self.track_tail()

        if self.y < 0:
            self.y = HEIGHT - self.height 
            self.track_tail()
        self.is_dead()
        for i in range(len(self.tail)):
            win.blit(self.img, self.tail[i])
        #pygame.display.update()
        #print(self.tail)      