# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:17:30 2019

@author: gyak
"""

import random
import operator
import matplotlib.pyplot

def distance_between(agents_row_a, agents_row_b):
    answer = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    return (answer)

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

## Move the agents.
#for j in range(num_of_iterations):
#    for i in range(num_of_agents):
#
#        if random.random() < 0.5:
#            agents[i][0] = (agents[i][0] + 1) % 100
#        else:
#            agents[i][0] = (agents[i][0] - 1) % 100
#
#        if random.random() < 0.5:
#            agents[i][1] = (agents[i][1] + 1) % 100
#        else:
#            agents[i][1] = (agents[i][1] - 1) % 100
#
#
#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.xlim(0, 99)
#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#matplotlib.pyplot.show()
#
#
#print(max(agents, key=operator.itemgetter(1)))


distance_all=[]
for j in range(num_of_agents):
    distance=[]
    for i in range(num_of_agents):
        distance.append (distance_between(agents[j], agents[i]))
    distance_all.append(distance)









