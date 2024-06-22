import pygame
import sys
import time
import random
import hero_modual

class Raindrop:
    def __init__(self, screen: pygame.surface, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        # Done 8: Initialize this Raindrop, as follows:
        #     - Store the screen.
        #     - Set the initial position of the Raindrop to x and y.
        #     - Set the initial speed to a random integer between 5 and 15.
        #   Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)
    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        # TODO 11: Change the  y  position of this Raindrop by its speed.
        self.y += self.speed


    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # TODO 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        return self.y > self.screen.get_height()


    def draw(self):
        """ Draws this sprite onto the screen. """
        # Done 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        #      from the current position of this Raindrop (use either a black or blue color).
        pygame.draw.line(self.screen, (0, 0, 0),(self.x, self.y),(self.x, self.y + 5) )



class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        # TODO 24: Initialize this Cloud, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Cloud to x and y.
        #     - Set the image of this Cloud to the given image filename.
        #     - Create a list for Raindrop objects as an empty list called raindrops.
        #   Use instance variables:
        #      screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []
    def draw(self):
        """ Draws this sprite onto the screen. """
        # TODO 25: Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        # TODO 28: Append a new Raindrop to this Cloud's list of raindrops,
        #     where the new Raindrop starts at:
        #       - x is a random integer between this Cloud's x and this Cloud's x + 300.
        #       - y is this Cloud's y + 100.
        new_drop = Raindrop(self.screen,
                            random.randint(self.x,  self.image.get_width()+ self.x),
                            self.y + self.image.get_height())

        self.raindrops.append(new_drop)

def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()
    pygame.display.set_caption("rainy day")
    screen = pygame.display.set_mode((1000,600))

    clock = pygame.time.Clock()
    # TODO 7: As a temporary test, make a new Raindrop called test_drop at x=320 y=10
    #test_drop = Raindrop(screen, 250, 10)
    # TODO 15: Make a Hero, named me, with appropriate images, starting at position x=200 y=400.
    # TODO 15: Make a Hero, named alyssa, with appropriate images, starting at position x=700 y=400.
    # TODO 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    mike = hero_modual.Hero(screen, 200, 400, "Mike_umbrella.png","Mike.png")
    alyssa = hero_modual.Hero(screen,700, 400, "Alyssa_umbrella.png ", "Alyssa.png" )
    cloud = Cloud(screen,300, 50, "cloud.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # TODO 27: Inside the game loop (AFTER the events loop above), get the list of keys that are currently pressed.
        #     Arrange so that the Cloud moves:
        #       5 pixels (or 10 pixels) to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        #       5 pixels (or 10 pixels) to the left  if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        #       5 pixels (or 10 pixels) up           if the Up    Arrow key (pygame.K_UP)    is pressed.
        #       5 pixels (or 10 pixels) down         if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        # DISCUSS: If you want something to happen once per key press, put it in the events loop above
        #          If you want something to continually happen while holding the key, put it after the events loop.
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x += 10
        if pressed_keys[pygame.K_LEFT]:
            cloud.x -= 10
        if pressed_keys[pygame.K_UP]:
            cloud.y -= 10
        if pressed_keys[pygame.K_DOWN]:
            cloud.y += 10

        screen.fill(pygame.Color("White"))
        # --- begin area of test_drop code that will be removed later
        # TODO 12: As a temporary test, move test_drop
        #test_drop.move()
        # TODO 14: As a temporary test, check if test_drop is off screen, if so reset the y position to 10

        # TODO 10: As a temporary test, draw test_drop
        #test_drop.draw()
        # TODO 20: As a temporary test, check if test_drop is hitting Mike (or Alyssa), if so set their last_hit_time

        # TODO 22: Remove the code that reset the y of the test_drop when off_screen()
        #          Instead reset the test_drop y to 10 when mike is hit, additionally set the x to 750
        #          Then add similar code to alyssa that sets her last_hit_time and moves the test_drop to 10 320
        # --- end area of test_drop code that will be removed later

        # TODO 26: Draw the Cloud.

        # TODO 29: Remove the temporary testdrop code from this function and refactor it as follows:
        # TODO: Make the Cloud "rain", then:
        # TODO    For each Raindrop in the Cloud's list of raindrops:
            #       - move the Raindrop.
            #       - draw the Raindrop.
            # TODO  30: if the Hero (Mike or Alyssa) is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            # Optional  - if the Raindrop is off the screen or hitting a Hero, remove it from the Cloud's list of raindrops.
        # TODO 18: Draw the Heroes (Mike and Alyssa)
        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()

            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)


        mike.draw()
        alyssa.draw()
        cloud.draw()
        # TODO 6: Update the display and remove the pass statement below
        pygame.display.update()
main()
# done 0: Call main.
