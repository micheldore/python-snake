from snake import Snake
import random
import pygame
import copy

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (0, 0)
screen = None
scaling_factor = 16

class Game:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, amount_snakes=2):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.snakes = []
        self.snakes = [Snake(self.randomLocation()) for _ in range(amount_snakes)]
        self.food = self.randomFood()

    def start(self,gui=True):
        def drawPixel(location, color):
            x,y=location
            pygame.draw.rect(screen, color, pygame.Rect(x*scaling_factor, y*scaling_factor, scaling_factor, scaling_factor))

        def drawFood():
            drawPixel(self.food, GREEN)

        def drawSnake(s):
            drawPixel(s.body[0], RED)
            for loc in s.body[1:]:
                drawPixel(loc, WHITE)

        if gui:
            pygame.init()
            size = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
            screen = pygame.display.set_mode(size)
            pygame.display.set_mode((self.SCREEN_WIDTH*scaling_factor, self.SCREEN_HEIGHT*scaling_factor))
            pygame.display.set_caption("Snake")
            screen.fill(BLACK)
            clock = pygame.time.Clock()

        done = False
        while not done:
            snakesToDelete = []
            for snake in self.snakes:
                if not snake.death and self.snakeCollision(snake):
                    snakesToDelete.append(snake)
                    for snake in snakesToDelete:
                        snake.body  = []
                        snake.death = True

            if gui:
                screen.fill(BLACK)
                [drawSnake(snake) for snake in self.snakes if not snake.death]
                drawFood()
                if event.type == pygame.QUIT:
                    done = True
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()

            if all([snake.death for snake in self.snakes]):
                done = True

            eating = False
            for snake in self.snakes:
                if not snake.death:
                    eating = self.foodCollision(snake)
                    snake.move(eating)

            if eating: self.food = self.randomFood()

            if gui:
                pygame.display.flip()
                clock.tick(30)

        if gui:
            pygame.quit()

    def randomLocation(self):
        (x,y) = (random.randint(0,self.SCREEN_WIDTH - 1),random.randint(0 + 4,self.SCREEN_HEIGHT))
        while any([any([(x,y-i) in s.body for i in range(len(s.body))]) for s in self.snakes]):
            (x,y) = (random.randint(0,self.SCREEN_WIDTH - 1),random.randint(0 + 4,self.SCREEN_HEIGHT))
        return (x,y)

    def randomFood(self):
        (x,y) = (random.randint(0,self.SCREEN_WIDTH),random.randint(0,self.SCREEN_HEIGHT))
        while any([(x,y) in s.body for s in self.snakes]):
            (x,y) = (random.randint(0,self.SCREEN_WIDTH),random.randint(0,self.SCREEN_HEIGHT))
        return (x,y)

    def checkCollision(self, loc1, loc2):
        return loc1==loc2

    def snakeCollision(self, snake):
        headx, heady = snake.body[0]
        snakes = copy.copy(self.snakes)
        snakes.remove(snake)
        if(headx<0 or headx>=self.SCREEN_WIDTH or heady<0 or heady>=self.SCREEN_HEIGHT):
            return True
        elif((headx,heady) in snake.body[1:]):
            return True
        elif any([(headx,heady) in s.body for s in snakes]):
            return True
        else:
            return False

    def foodCollision(self, snake):
        return not snake.death and self.checkCollision(snake.body[0], self.food)

Game(40,40).start(gui=False)
