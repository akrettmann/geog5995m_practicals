# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:46:48 2019

@author: gyak
"""
import random

#create a class of agents which defines what the attributes of the agents are
 

class Agent():
#call init function 
    def __init__(self, ants, environment):
#calculate length of rows and columns         
        nrows = len(environment)
        ncols = len(environment[0])
#Setting x and y value to be a random integer between 0 and the length and rows of columns
        self.x = random.randint(0,ncols - 1)
        self.y = random.randint(0,nrows -1)
#        
        self.store = 0
        self.agents = ants
#sheep in this case 
        self.environment = environment
# in this example, all agents are part of the same environment 

        pass

    
    def move(self):
        """
        Move agent with conditional statement
        """
    
        nrows = len(self.environment)
        ncols = len(self.environment[0])
        if random.random() < 0.5:
            self.x = self.x + 1 % ncols
        else:
            self.x = self.x - 1 % ncols
        if random.random() < 0.5:
            self.y = self.y + 1 % nrows
        else:
            self.y = self.y - 1 % nrows