import pygame
from utilities.parameters import BLACK, HEIGHT, WHITE, WIDTH, snake_img, snake_head_img, background_img

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Consolas", 50)
game_over_message = font.render("Game Over", True, WHITE)
win_message = font.render("You win", True, 50)

dead_sound = pygame.mixer.Sound("sounds\\dead.wav")

class Snake:
    def __init__(self, x, y):
        self.head = snake_head_img
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
        self.menu = False

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

    def win_game(self, win):
        if len(self.tail) >= (WIDTH // self.width) ** 2:
        #if self.tail_len >= (WIDTH // self.width) ** 2:
            self.tail = [(self.x, self.y)]
            self.tail_len = 1
            self.menu = True
            #win.fill(BLACK)
            win.blit(background_img, (0, 0))
            win.blit(win_message, (WIDTH // 2 - win_message.get_width() // 2,
            HEIGHT // 2 - win_message.get_height() // 2))
            pygame.display.update()
            pygame.time.wait(1000)

    def is_dead(self, win):
        if (self.x, self.y) in self.tail[0:(len(self.tail) - 1)]:
            self.tail = [(self.x, self.y)]
            self.tail_len = 1
            self.menu = True
            #win.fill(BLACK)
            pygame.mixer.Sound.play(dead_sound)
            win.blit(background_img, (0, -HEIGHT))
            win.blit(game_over_message, (WIDTH // 2 - game_over_message.get_width() // 2,
                                        HEIGHT // 2 - game_over_message.get_height() // 2))
            pygame.display.update()
            pygame.time.wait(1000)
            #return True
        #return False

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
        if self.is_key_pressed(pygame.K_w, event) or self.is_key_pressed(pygame.K_UP, event):
            self.direction = "up"
        if self.is_key_pressed(pygame.K_s, event) or self.is_key_pressed(pygame.K_DOWN, event):
            self.direction = "down"
        if self.is_key_pressed(pygame.K_a, event) or self.is_key_pressed(pygame.K_LEFT, event):
            self.direction = "left"
        if self.is_key_pressed(pygame.K_d, event) or self.is_key_pressed(pygame.K_RIGHT, event):
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

        self.is_dead(win)
        self.win_game(win)

        for i in range(len(self.tail)):
            win.blit(self.head, self.tail[-1])
            if i != len(self.tail) - 1:
                win.blit(self.img, self.tail[i])
        #pygame.display.update()
        #print(self.tail)      