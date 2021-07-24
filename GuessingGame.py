#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 00:15:54 2018

@author: oguzhan
My first program - Guessing Game written in Python3
"""

while True: # First, we taking the inputs for range and if it is not valid
    #values we ask again for range
    begin = input('Begin: ')
    end = input('End: ')

    try: # This will check users inputs are integers or not
        begin = int(begin)
        end = int(end)

        if begin <= 0 or end <= 0: # If the inputs are negative
            print('You have to enter positive numbers for the range! ')
            continue # Loops for range

        if begin > end: #This will check our begin is smaller than end or not
            print('Begin can not bigger than the end! ')
            continue

        S = 100 # Starting point of the game
        N = (end - begin) * 0.2 # Number of guesses user have
        N = round(N) # If %20 of range is not a integer this will round it

        if end - begin < 2.5: #This is for the smaller ranges
            N = 1
            break

        else:
            break

    except: # Loops if user gives invalid input
        print('You need to enter integers')
        continue

# Then we need to set the target

import random # This will import the random module for below line
target = random.randint(begin,end) # This will set target to random integer

# And the game is starting

while N != 0 or S != 0: # If number of guesses or score becomes 0,
                        #then player loses.

    print('The target is in [', begin, ',' ,end , '] You have ' ,
          N ,'guesses...') # Prints the range and number of guesses
    guess = input('Your guess: ') # Taking a guess from player

    try: # Checks the guess is integer or not
        guess = int(guess)
    except: # If guess is an integer, then this will not executed
        print('You need to enter a integer for guess!')
        continue # If guess is not an integer, then loops for another guess

    if begin > guess or guess > end: # If the guess is not in the range
        print('Your guess not even in the range! ')
        continue # Loops if it is not in the range

    if guess == target: # If player enters right guess, then the game finishes
        print('Right guess! Score: ', S)
        break # For exiting from loop when player wins
    else: # If guess is wrong, then loses points and number of guess
        print('Wrong guess!')
        N -= 1
        S -= 5

    if N == 0: # Block which reduces range randomly
        distance = end - begin

        if end - target > target - begin: # If target close to begin
            begin = random.randint(begin, target)
            end = int(begin + distance / 2)
        else: # If target close to end
            end = random.randint(target, end)
            begin = int(end - distance / 2)

        N = (end - begin) * 0.2 # New number of guess player have
        N = round(N) # Sometimes %20 of a number can be float

    if N == 0 or S == 0: # When points or number of guesses totally run out
        print('You lost! The target was ', target, '.')
        break # Player loses
    else:
        continue # Loop for another guess
