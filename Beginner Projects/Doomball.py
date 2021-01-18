# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:47:10 2019

@author: Rahul
"""
import math
import random
 
def print_instructions():
    print(""" Welcome to DoomBall! The idea is to hit the target with a doomball.
          Enter your angle(in degrees) and the amount of PSI to charge your gun with. """ )
     
def calculate_distance(psi,angle_in_degrees):
    angle_in_radians = math.radians(angle_in_degrees)
    distance = .5 * psi ** 2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)
    return distance
def get_user_input(name):
    psi = float(input(name + " charge the gun with how much psi ?"))
    angle = float(input(name + " move the gun at what angle ?"))
    return psi,angle
def get_player_names():
    print("Enter player names.Enter as many as you like.")
    done = False
    players = []
    while not done:
        player = input("Enter player (hit enter to quit):")
        if len(player) > 0:
            players.append(player)
        else:
            done = True
            
        print()
        return players

def process_player_turn(player_name,distance_apart):
    psi,angle = get_user_input(player_name)
    distance_mudball = calculate_distance(psi,angle)
    difference = distance_mudball - distance_apart
    if difference > 1:
        print("You went", difference,"yards too far!")
    elif difference < -1:
        print("You were", difference * -1,"yards too short!")
    else:
        print("Hit!!",player_name,"wins!!")
        return True
    
    print()
    return False
def main():
    print_instructions()
    player_names = get_player_names()
    distance_apart = random.randrange(50,150)
    done = False
    while not done:
        for player_name in player_names:
            done = process_player_turn(player_name,distance_apart)
        if done:
            break
        
if __name__ == "__main__":
  main()
