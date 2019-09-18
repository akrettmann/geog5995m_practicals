# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:39:31 2019

@author: gyak
"""

import matplotlib.pyplot
import operator
import random

num_of_agents = 10
num_of_iterations = 100

y0=random.randint (0,100)
x0=random.randint (0,100)

agents = []
agents.append([y0,x0])
agents[0][0]
agents[0][1]
print (agents)

y1=random.randint (0,100)
x1=random.randint (0,100)
agents.append([y1,x1])
agents[1][0]
agents[1][1]
print (agents)

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

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



'''
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
'''

#answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
#print(agents[0][0], agents[0][1], agents[1][0], agents[1][1], answer)

agents.append([random.randint(0,99),random.randint(0,99)])

print(max(agents))
print(max(agents, key=operator.itemgetter(1)))

#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
#matplotlib.pyplot.show()

matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()

for j in range(num_of_iterations):
    
    

    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] += 1
        else:
            agents[i][0] -= 1
    
        if random.random() < 0.5:
            agents[i][1] += 1
        else:
            agents[i][1] -= 1


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    
    

if random.random() < 0.5:
    agents[i][0] = (agents[i][0] + 1) % 100
else:
    agents[i][0] = (agents[i][0] - 1) % 100













