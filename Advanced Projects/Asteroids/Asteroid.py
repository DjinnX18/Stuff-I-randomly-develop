# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:43:42 2021

@author: Rahul
"""
import pygame
from Utility import load_sprite, get_random_position,print_text
from Sprite import Spaceship,Asteroid
class Asteroids:
    MIN_ASTEROID_DISTANCE = 250
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800,600))
        self.background = load_sprite("space", False)
        self.bullet = []
        self.spaceship = Spaceship((400,300), self.bullet.append)
        self.clock = pygame.time.Clock()
        self.asteroid = []
        self.font = pygame.font.Font(None, 64)
        self.message = ""
        
        for _ in range(6):
            while True:
                position = get_random_position(self.screen)
                if (position.distance_to(self.spaceship.position) 
                > self.MIN_ASTEROID_DISTANCE):
                    break
            self.asteroid.append(Asteroid(position,self.asteroid.append))    
                    
    def main_loop(self):
        while True:
            pygame.event.pump()
            self._handle_input()
            self._process_game_logic()
            self._draw()
            
    def _get_game_objects(self):
        game_object = [*self.asteroid, *self.bullet]
        if self.spaceship:
            game_object.append(self.spaceship)
        return game_object    
        
        
        
            
    def _init_pygame(self):
        pygame.init() # This initializes pygame and its features
        pygame.display.set_caption("Asteroids 2.0")
        
    def _handle_input(self):
        for event in pygame.event.get(): # pygame.event.game()
            if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
            elif (
                self.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.spaceship.shoot()
                
        is_key_pressed = pygame.key.get_pressed()
        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            if  is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()
            if is_key_pressed[pygame.K_DOWN]:
                self.spaceship.decelerate()
    
    def _process_game_logic(self):
       for game_object in self._get_game_objects():
        game_object.move(self.screen)
        
       if self.spaceship:
           for asteroid in self.asteroid:
               if asteroid.collides_with(self.spaceship):
                   self.spaceship = None
                   self.message = "You Lost!"
                   break
       for bullet in self.bullet[:]:
            for asteroid in self.asteroid[:]:
                if asteroid.collides_with(bullet):
                    self.asteroid.remove(asteroid)
                    self.bullet.remove(bullet)
                    asteroid.split()
                    break    
       for bullet in self.bullet[:]:
        if not self.screen.get_rect().collidepoint(bullet.position):
            self.bullet.remove(bullet)  
       
       if not self.asteroid and self.spaceship:
           self.message = "You Won!"
    
    def _draw(self):
        self.screen.blit(self.background, (0, 0))

        for game_object in self._get_game_objects():
            game_object.draw(self.screen)
            
        if self.message:
            print_text(self.screen, self.message, self.font)

        pygame.display.flip()
        self.clock.tick(60)
        
            
    
