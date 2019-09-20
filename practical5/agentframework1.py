# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:46:48 2019

@author: gyak
"""
import random

#create a class of agents which defines what the attributes of the agents are
 

class Agent():
#call init function 
    def __init__(self, name, ants, environment):
#calculate length of rows and columns         
        self.name = name
        nrows = len(environment)
        ncols = len(environment[0])
#Setting x and y value to be a random integer between 0 and the length and rows of columns
        self.x = random.randint(0,ncols - 1)
        self.y = random.randint(0,nrows -1)
        self.canshare = 'true'
        #self.x = x
        #self.y = y
#        
        self.store = 0
        self.agents = ants
#sheep in this case 
        self.environment = environment
# in this example, all agents are part of the same environment 

        pass

    def __str__(self):
        return "Hi I am agent " + str(self.name) + " with store " + str(self.store)


    def move(self):
        """
        Move agent with conditional statement
        """
    
        nrows = len(self.environment)
        ncols = len(self.environment[0])
        if random.random() < 0.5:
            self.x = (self.x + 1) % ncols
        else:
            self.x = (self.x - 1) % ncols
        if random.random() < 0.5:
            self.y = (self.y + 1) % nrows
        else:
            self.y = (self.y - 1) % nrows
            
            
    def distance_between(self, i):
        """
        
        """
        return (((self.x - self.agents[i].x)**2) +
        ((self.y - self.agents[i].y)**2))**0.5           
         
    def eat(self, amount_eaten):
        value = self.environment[self.x][self.y]
        #amount_eaten = 11
        if value > amount_eaten:
            self.store = self.store + amount_eaten
            self.environment[self.x][self.y] = value - amount_eaten
            print("Value eaten", amount_eaten)
            
    def share(self, neighbourhood):
        for i in range(len(self.agents)):
            if i != self.name:
                distance = self.distance_between(i)
                if distance < neighbourhood:
                    average = (self.store + self.agents[i].store) /2
                    print(self)
                    print(" sharing with agent",i,"my store", self.store, "their store", self.agents[i].store, "amount shared", average)
                    self.store = average
                    self.agents[i].store = average        
        
        
        
print ("Hello World")