# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:39:20 2020

@author: ghanshyam

"""
import sys
''' We use sys tool for game exit'''

import pygame

from settings import Settings
from ship import Ship # use after ship.py
from bullet import Bullet

class AlienInvasion:
    '''Initialize the game ,and create game resource'''
    def __init__(self):
        pygame.init()  #pygame init for pygame work properly
        
        self.settings = Settings() # baad me use kiya settings.py bnane ke baad
        
        # For full screen
  #     self.screen =pygame.display.set_mode((0, 0)), pygame.FULLSCREEN)
  #     self.settings.screen_width = self.screen.get_rect().width
  #     self.settings.screen_height = self.screen.get_rect().height
        
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))#this is also know as surface
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self) # use after ship.py
        self.bullets = pygame.sprite.Group()

        
        '''Setting background colour, humne baad me use kiya ye code'''
        self.bg_colour = (230, 230, 230)
        
    def run_game(self):
         '''start the main loop for the game'''
         while True:
             self._check_events() # this add for clicking by user ,after third modification
             self.ship.update() # this add in fifth modification
             self.bullets.update()
             self._update_screen() # add in third modification
             

    def _check_events(self):         
             # Watch for keyboard and mouse
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     sys.exit()
                 elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                 elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)
                     
    def _check_keydown_events(self,event):
            '''Respond to keypress.'''
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
                
    def _check_keyup_events(self, event):
            '''Respond to key relese.'''
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
   
        # move ship to the right
            self.ship.rect.x += 1
            
    def _fire_bullet(self):
        # Get rid of bullets that have disapered.
        for bullet in self.bullets.copy():
                 if bullet.rect.bottom <= 0:
                     self.bullets.remove(bullet)
             #print(len(self.bullets)) see to how many bullets remove
        
        '''create new bullet and it to the bullets group.'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)        
                
    def _update_screen(self):                 
             self.screen.fill(self.settings.bg_color) 
             self.ship.blitme()
             for bullet in self.bullets.sprites():
                 bullet.draw_bullet()
                     
             pygame.display.flip() # This is use for flip screen after use       
                     

            # Make the most recently drawn screen visible.
            
if __name__ == '__main__':
  #Make a game instance, run the game.
    ai = AlienInvasion()
    ai.run_game()  
         