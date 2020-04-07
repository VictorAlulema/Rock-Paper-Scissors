# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:52:41 2020

@author: victor
"""

import random
from sys import exit

def initial_values():
    
    Human = input('Give and int between 1 and 10')
    exit_routine(Human)
    My_PC = random.randint(1,10)
    return Human , My_PC

def players_value(Human,My_PC):
    print('PC {} --- User {} ---'.format(Human,My_PC))

def who_begins():
    """ This funcion permits to determine who begins to play """
    while True:
        Human, My_PC = initial_values()
        try:
            if int(Human) > My_PC and int(Human) <= 10:
                Flag = True
                players_value(Human,My_PC)        
                break
            elif int(Human) < My_PC and int(Human) >=1:
                Flag = False
                players_value(Human,My_PC)
                break
            else:
                players_value(Human,My_PC)
                print('Try again!')
        except ValueError:
            players_value(Human,My_PC)
            print('Try again!')
    return Flag
    
def human_play():
    """ Request the human choice 
    and incorporates a simple text prediction routine"""
    word_set = ['rock', 'paper', 'scissors']
    while True:
        human_input = input('Choose: rock, paper, scissors')
        exit_routine(human_input)
        if human_input in word_set:
            break
        else:
            predictive_text(word_set,human_input,count=0)
    return human_input

def PC_play():
    options = ['rock', 'paper', 'scissors']
    index =  random.randint(0,2)
    return options[index]

def predictive_text(word_set,human_input,count=0):
    for word in word_set:
        for char in human_input:
            count = char_count(char,word,count) 
        coincidence = (count / len(word)) * 100
        if coincidence in range(75,100):
            print('Did you mean {}?'.format(word))  
        else:
            pass 
    print('Try again')
        
def char_count(char,word,count):
    if char in word:
        count = count + 1                
    else:
        pass
    return count

def exit_routine(string):
    if string == 'exit':
        exit()
    else:
        pass
    
def who_wins(human,my_pc):
    if human == my_pc:
        print('No winner')
    elif human == 'paper' and my_pc == 'rock':
        print('{} wins'.format('human'))    
    elif human == 'rock' and my_pc == 'scissors':
        print('{} wins'.format('human'))
    elif human == 'scissors' and my_pc== 'paper':
        print('{} wins'.format('human'))
    elif my_pc == 'paper' and human == 'rock':
        print('{} wins'.format('My_PC'))    
    elif my_pc == 'rock' and human == 'scissors':
        print('{} wins'.format('My_PC'))
    elif my_pc == 'scissors' and human == 'paper':
        print('{} wins'.format('My_PC'))
    print('New game')

if __name__ == "__main__":
    while True:
        Turn = who_begins()
        if Turn == True:
            print('human begins....!')
            human = human_play()
            my_pc = PC_play()
            who_wins(human,my_pc)
            print()
        else:
            print('PC begins....!')
            my_pc = PC_play()
            human = human_play()
            who_wins(human,my_pc)
            
