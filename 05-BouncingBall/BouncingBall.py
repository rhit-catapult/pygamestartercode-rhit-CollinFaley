import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.



class Cloud:
    def __init__(self, screen, x, y, image_filename):

        self.screen = screen
        self.x = x
        self.y = y
        self.Balls = []
    def rain(self):

        new_Ball = Ball(self.screen)

        self.Balls.append(new_Ball)




class Ball:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = random.randint(100,screen.get_width()-100)
        self.y = random.randint(100,screen.get_height()-100)
        self.speedx = random.randint(5, 15)
        self.speedy = random.randint(5, 15)
        self.raidius = random.randint(10,100)
        self.color = pygame.Color(random.randint(0,255),
                                  random.randint(0,255),
                                  random.randint(0,255))
    def move(self):
        self.y += self.speedy
        self.x += self.speedx

        if self.x >= 1000 - self.raidius:
            self.speedx *= -1
            pygame.mixer.Sound("Drums.wav").play()
        if self.y >= 600 - self.raidius:
            self.speedy *= -1
            pygame.mixer.Sound("Drums.wav").play()
        if self.x <= 0 + self.raidius:
            self.speedx *= -1
            pygame.mixer.Sound("Drums.wav").play()
        if self.y <= 0 + self.raidius:
            self.speedy *= -1
            pygame.mixer.Sound("Drums.wav").play()
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.raidius)



# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class called ball1
    #ball1 = Ball(screen)
    Balls = []
    for I in range(0,15):
        new_ball = Ball(screen)
        Balls.append(new_ball)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(60)

        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        # TODO: Draw the ball

        for ball in Balls:
            ball.move()
            ball.draw()


       # ball1.move()
       # ball1.draw()



        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
