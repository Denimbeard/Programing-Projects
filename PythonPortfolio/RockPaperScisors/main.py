#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author Details
# =============================================================================
__author__ = 'Chet Coenen'
__copyright__ = 'Copyright 2020'
__credits__ = ['Chet Coenen']
__license__ = '/LICENSE'
__version__ = '0.1'
__status__ = 'Under Development'
# ==============================================================================
# Contact
# ==============================================================================
__maintainer__ = 'Chet Coenen'
__email__ = 'chet.m.coenen@icloud.com'
__socials__ = '@Denimbeard'
__username__ = 'Denimbeard'
# =============================================================================
# Project Data
# =============================================================================
__course__ = ''
__date__ = '23/01/2021'
__teammates__ = ['Chet Coenen']
__laboratory__ = ''
__description__ = 'Rock, Paper, Scissors'
__studentid__ = '33683213'

# =============================================================================
import time
import random

class game:
    score = 0
    rule = 'Rock Beats Scissors, Paper Beats Rock, Scissors Beats Paper.'

    def __init__(self, player):
        self.player = player
    
    def rules():
        r = input('Need rules? y/n: ')
        if r == 'y':
            return game.rule

    def score(self):
        return '{} {}'.format(self.player, self.score) 

    def play(self):
        var = ['Rock', 'Paper', 'Scissors']
        comp = random.choice(var)
        pv = input('Shoot! \n')
        print(pv + ' vs ' + comp)
        if comp == 'Rock':
            if var == 'Paper':
                

p1 = game('Player 1')
comp = game('Computer')

print(game.rules())
print(game.play(p1))