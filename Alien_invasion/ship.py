import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        #initilize the ship and define its starting position
        self.screen = screen
        self.ai_settings = ai_settings

        #loading ship image and getting rectangle
        self.image = pygame.image.load('Images/DurrrSpaceShip.png') 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #every new ship appear on down of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #saving float ship's coordinates
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.right > 50:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center


    def blitme(self):
        #draw ship in current position
        self.screen.blit(self.image, self.rect)
    




