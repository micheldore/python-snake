import pygame

class GUI:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, scaling_factor, on=True):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.scaling_factor = scaling_factor
        self.on = on
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        if on:
            pygame.init()
            size = (SCREEN_WIDTH, SCREEN_HEIGHT)
            self.screen = pygame.display.set_mode(size)
            pygame.display.set_mode((SCREEN_WIDTH*scaling_factor, SCREEN_HEIGHT*scaling_factor))
            pygame.display.set_caption("Snake")
            self.screen.fill(self.BLACK)
            self.clock = pygame.time.Clock()


    def iteration(self, gamestate):
        if self.on:
            self.setScreen(self.BLACK)
            [self.drawSnake(snake) for snake in gamestate.snakes if not snake.death]
            self.drawFood(gamestate.food)
            pygame.display.flip()
            self.clock.tick(30)
        return self.checkToQuit() or all([snake.death for snake in gamestate.snakes])

    def drawPixel(self, location, color):
        if self.on:
            x,y=location
            pygame.draw.rect(self.screen, color, pygame.Rect(x*self.scaling_factor, y*self.scaling_factor, self.scaling_factor, self.scaling_factor))

    def drawFood(self, food):
        if self.on:
            self.drawPixel(food, self.GREEN)

    def drawSnake(self, snake):
        if self.on:
            self.drawPixel(snake.body[0], self.RED)
            for loc in snake.body[1:]:
                self.drawPixel(loc, self.WHITE)

    def setScreen(self, color):
        if self.on: self.screen.fill(color)

    def checkToQuit(self):
        if self.on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
        return False

    def quit(self):
        if self.on: pygame.quit()
