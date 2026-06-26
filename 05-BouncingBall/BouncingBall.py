import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class Ball():
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.x_speed = random.randint(1,25)
        self.y_speed = random.randint(1,25)
        # self.speed.x = random.randint(1,25)
        # self.speed.y = random.randint(1,25)
    def move(self):
        self.y = self.y + self.y_speed
        self.x = self.x + self.x_speed
    def draw(self):
        pygame.draw.circle(self.screen, (random.randint(0,225),random.randint(0,225),random.randint(0,225)), (self.x, self.y), (random.randint(10,20)))

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class called ball1
    ball1 =  Ball(screen,random.randint(0,screen.get_width() - 20),random.randint(0,screen.get_width() - 20),)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(1)
        screen.fill(pygame.Color('gray'))
        
        # TODO: Move the ball
        # TODO: Draw the ball
        # ball1.move()
        ball1.draw()
        pygame.display.update()
main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
