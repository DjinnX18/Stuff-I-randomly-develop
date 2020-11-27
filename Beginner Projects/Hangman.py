# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:56:57 2020

@author: Swindell17520
"""
import random
print(""""Welcome to Hangman!! In this game you will have to guess the secret word
          before a certain number of turns in order to win.""")
      
name = input("Please enter your name:-")
print("Hello",name,"Welcome to Hangman! Try to guess the word within 12 turns!")
words = ['bumblebee','agentspeak','apple','rainbow', 'computer', 'science', 'programming', 
         'python', 'mathematics', 'player', 'condition', 
         'reverse', 'water', 'board', 'geeks']
secret_word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 12
while turns > 0:
    failed = 0
    for char in secret_word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed +=1
    if failed == 0:
        print("You win!!!!")
        print("The word was:",secret_word)
        break
    guess = input("Guess a character:")
    guesses+=guess
    if guess not in secret_word:
        turns-=1
        print("Wrong character. Try again")
        print("You have",turns,"guesses left.")
        
    if turns == 0:
        print("Sorry, you have lost the game")
        print("The word was:",secret_word)
        
        
            
    
      


