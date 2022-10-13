import pygame

class Ship():
    
    def __init__(self,screen):
        #initilize the ship and define its starting position
        self.screen = screen

        #loading ship image and getting rectangle
        self.image = pygame.image.load('Images/DurrrSpaceShip.png') 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #every new ship appear on down of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        #draw ship in current position
        self.screen.blit(self.image, self.rect)
    




