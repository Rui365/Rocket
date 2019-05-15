import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/rsz_rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        self.center = float(self.rect.centerx)
        self.centerho = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centerho += self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centerho -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.centery = self.centerho


    def blitme(self):
        self.screen.blit(self.image,self.rect)