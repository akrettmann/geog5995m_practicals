# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:39:31 2019

@author: gyak
"""

import matplotlib.pyplot
import operator
import random

agents = []

number_of_agents = 2

seed = 101
random.seed(seed)

for i in range (0, number_of_agents):
    x = random.randint(0,99)
    print("x",x)
    y = random.randint(0,99)
    print("y",y)
    z = random.randint(0,99)
    print("z",z)
    agent = []
    agent.append(x)
    agent.append(y)
    agent.append(z)
    #agent = [x, y, z]
    agents.append(agent)

print(agents)





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


agents = []
agents.append([y0,x0])
agents[0][0]
agents[0][1]
print (agents)


y1=random.randint (0,99)
x1=random.randint (0,99)
agents.append([y1,x1])
agents[1][0]
agents[1][1]
print (agents)






#y0=50 
#x0=50 
#if random.random() < 0.5:
 #   y0 = y0 + 1
#else:
 #   y0 = y0 - 1
#print (y0)
#
#if random.random() < 0.5:
#    x0 = x0 + 1
#else:
#    x0 = x0 - 1
#print (x0)
#y1=50 
#x1=50 
#if random.random() < 0.5:
#   y1 = y1 + 1
#else:
#    y1 = y1 - 1
#print (y1)
#
#if random.random() < 0.5:
#    x1 = x1 + 1
#else:
#    x1 = x1 - 1
#print (x1)
#
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

print(max(agents))
print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.show()





















'''