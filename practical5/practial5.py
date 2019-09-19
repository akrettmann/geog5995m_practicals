import random
import operator
import matplotlib.pyplot
import agentframework
import csv

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Initialise environment
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
nrows = len(environment)
print("nrows", nrows)
ncols = len(environment[0])
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
        

