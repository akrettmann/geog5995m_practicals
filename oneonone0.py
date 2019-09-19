# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:39:31 2019

@author: gyak
"""

import matplotlib.pyplot
import operator
import random
import time

def distance_between(a, b):
    """
    This calculates the distance between a and b where a and b are lists with 
    two coordinates.
    
    Parameters
    ----------
    a
        A list containing two coordinates
    b   A list containing two coordinates

    Returns
    -------
    a numerical distance
    """
    answer = (((a[0] - b[0])**2) + ((a[1] - b[1])**2))**0.5
    return answer

def move(a):
    """
    Move agent
    
    Parameters
    ----------
    a
        A list containing two coordinates
    """
    if random.random() < 0.5:
        a[0] = a[0] + 1
    else:
        a[0] = a[0] - 1
    if random.random() < 0.5:
        a[1] = a[1] + 1
    else:
        a[1] = a[1] - 1

# start is the begining time and is used to time how long things take 
start = time.process_time()

# seed is used to set the start of the pseudorandom sequence.
# changing seed will change the results of calling random functions
# To run for a variety of results run the program for different seeds.
# Fixing the seed helps for debugging as it ensures that we are always dealing
# with the same values for variables.
seed = 102
random.seed(seed)

#Create an empty agents list
agents = []

#add written coordinates to the list
#agents.append([-1,-1])
agents.append([20,0])
print(agents)
move(agents[0])
print(agents)

#agents.append([3,2])
#agents.append([0,0])
agents.append([0,20])
agents.append([80,87])

#create a variable to define number of agents required (this is changable)
number_of_agents = 100

#create for loop to create random coordinates (agents) and add them to the empty list
#Will run for number of agents defined
for i in range (0, number_of_agents):
    x = random.randint(0,99)
    #print("x",x)
    y = random.randint(0,99)
    #print("y",y)
    #z = random.randint(0,99)
    #print("z",z)
    agent = []
    agent.append(x)
    agent.append(y)
    #agent.append(z)
    #agent = [x, y, z]
    agents.append(agent)

#calculating the length (len) of the agents list (number of agents)
print("agents",agents)
print("len(agents)",len(agents))
print("type(agents)",type(agents))

print("agents[0]", agents[0])
print("len(agents[0])",len(agents[0]))
print("agents[1]",agents[1])
print("len(agents[1])",len(agents[1]))

#calculating the max and the min distance between agents 
max_distance = distance_between(agents[0], agents[1])
min_distance = distance_between(agents[0], agents[1])
#for loop to remove distance calculation for same y and x coordinates (removes 0)
for i in range(0,len(agents)):
    for j in range(i,len(agents)):
        #print ("i", i,"j", j)
        #answer = (((agents[i][0] - agents[i+1][0])**2) + 
        #          ((agents[i][1] - agents[i+1][1])**2))**0.5
        answer = distance_between(agents[i], agents[j])
        #print("Distance between agent", i, "and agent", j, "is", answer)
        if (i != j):
            max_distance = max(max_distance, answer)
            #print("max_distance", max_distance)
            min_distance = min(min_distance, answer)
            #print("min_distance", min_distance)

#calculate time to process code. See what the difference is by changing number of agents. 
#aim is to simply code to reduce running time            
print("max_distance", max_distance)
print("min_distance", min_distance)
end = time.process_time()
duration = end - start
print("total time taken to calculate distances between initial agents", duration)

start1 = end
          
#print(max(agents))
#print(max(agents, key=operator.itemgetter(0)))

matplotlib.pyplot.ylim(-2, 99)
matplotlib.pyplot.xlim(-2, 99)

top_most_colour = 'yellow'
right_most_colour = 'pink'
bottom_most_colour = 'orange'
left_most_colour = 'red'


colours = []
#colours.append('#4B6F36')
colours.append('blue')
colours.append('green')
colours.append('grey')
colours.append('black')
colours.append('purple')

iteration = 10
for j in range(iteration):
    for i in range(len(agents)):
        move(agents[i])
        #print("i",i)
        k = i % len(colours)
        #print("k", k)
        top_most_agent = max(agents, key=operator.itemgetter(0))
        right_most_agent = max(agents, key=operator.itemgetter(1))
        bottom_most_agent = min(agents, key=operator.itemgetter(0))
        left_most_agent = min(agents, key=operator.itemgetter(1))
        matplotlib.pyplot.scatter(agents[i][1],agents[i][0], s=None, c=colours[k])
        matplotlib.pyplot.scatter(top_most_agent[1],top_most_agent[0], s=None, c=top_most_colour)
        matplotlib.pyplot.scatter(right_most_agent[1],right_most_agent[0], s=None, c=right_most_colour)
        matplotlib.pyplot.scatter(bottom_most_agent[1],bottom_most_agent[0], s=None, c=bottom_most_colour)
        matplotlib.pyplot.scatter(left_most_agent[1],left_most_agent[0], s=None, c=left_most_colour)
        
matplotlib.pyplot.show()
         
end = time.process_time()
duration_of_plotting = end - start1
print("total processing time", duration_of_plotting)
duration = end - start
print("total processing time", duration)

   
'''
<Code to understand loops and conditional if statements>
for i in range(0,3):
    seed = 100 * i
    random.seed(seed)
    y0=random.randint(0, 99)
    x0=random.randint(0, 99)
    print("Random seed", seed)
    condition = (seed == 100)
    condition1 = (seed > 100)
    print("Is Random seed equal to 100?",condition)
    if condition:
        print("y0",y0)
        print("x0",x0)
    elif condition1:
        print("Aha, this must be seed > 100!")
    elif condition2:
                
    else:
        print("Not telling you the values.")
</Code to understand loops and conditional if statements>
'''


'''
y0=50 
x0=50 
if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print (y0)

if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print (x0)
y1=50 
y1=50 
if random.random() < 0.5:
   y1 = y1 + 1
else:
    y1 = y1 - 1
print (y1)
if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print (x1)

#answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
#print(y0, x0, y1, x1, answer)



if random.random() < 0.5:
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1
print (agents[0][0])

if random.random() < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1
print (agents[0][1])
#y1=50 
#x1=50 
if random.random() < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1
print (agents[1][0])

if random.random() < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1
print (agents[1][1])

answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(agents[0][0], agents[0][1], agents[1][0], agents[1][1], answer)

agents.append([random.randint(0,99),random.randint(0,99)])


'''

