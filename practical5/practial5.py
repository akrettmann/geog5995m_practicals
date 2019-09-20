import random
import operator
import matplotlib.pyplot
import agentframework
import csv

#create function to calculate distance between each of the agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

#create variable for the number of agents and iterations 
#create an empty list for the agents
num_of_agents = 10
num_of_iterations = 100
agents = []

# Initialise environment
#Create variable for environment to read file into using CSV reader 
#(converts text into numbers)
environment = []
with open("../in.txt") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        environment_row = []
        #print(row)
        for value in row:
            #print(value)
            environment_row.append(int(value))
        environment.append(environment_row)
#Determine number of columns and rows 
nrows = len(environment)
print("nrows", nrows)
ncols = len(environment[0])
#Create for loop to check if same number of columns as rows exist
for row in range(0,nrows):
    ncols_row = len(environment[row])
    if ncols != ncols_row:
        print("Urgh, data not rectangular")
print("ncols", ncols)
print(environment[nrows - 1][ncols - 1])

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(agents, environment))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        matplotlib.pyplot.scatter(agents[i].y,agents[i].x)
matplotlib.pyplot.xlim(0, ncols - 1)
matplotlib.pyplot.ylim(0, nrows -1)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        

