# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:56:33 2020

@author: ghanshyam
"""

''' this is setting class which we use through this entire project'''

class Settings:
    '''this class to store all the setting for Alien Invasion.'''
    
    def __init__(self):
        '''Initialize the game's settings.'''
        self.screen_width = 1200
        self.screen_height= 800
        self.bg_color = (230, 230, 230)
        
        #Ship setting
        self.ship_speed = 1.5 #add on 6th modification
        
        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        #limiting bullet  making group of 3 bullet on screen
        self.bullets_allowed = 3