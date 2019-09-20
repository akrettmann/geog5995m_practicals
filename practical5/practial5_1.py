import random
import operator
import matplotlib.pyplot
import agentframework
import csv

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 10
agents = []

# seed is used to set the start of the pseudorandom sequence.
# changing seed will change the results of calling random functions
# To run for a variety of results run the program for different seeds.
# Fixing the seed helps for debugging as it ensures that we are always dealing
# with the same values for variables.
seed = 102
random.seed(seed)

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
    #agents.append(agentframework.Agent(agents, environment), 3, 4)
    agents.append(agentframework.Agent(i, agents, environment))
    

sumenv = 0
for row in range(0,nrows):
    for col in range(0,ncols):
        sumenv += environment[row][col]
        #sumenv = sumenv + environment[row][col]
print("sumenv before eating",sumenv)

sumenv0 = sumenv
        
total_store = 0
for i in range(num_of_agents):
    total_store += agents[i].store
print("total_store before eating",total_store) 

max_amount_eaten = 10
for i in range(num_of_agents):
    amount_eaten = random.randint(0, max_amount_eaten)
    agents[i].eat(amount_eaten)
    
#agents.append(agentframework.Agent(agents, environment, 0, 0))
#agents.append(agentframework.Agent(agents, environment, 3, 4))

distance = agents[0].distance_between(1)
print("distance", distance)

sumenv = 0
for row in range(0,nrows):
    for col in range(0,ncols):
        sumenv += environment[row][col]
        #sumenv = sumenv + environment[row][col]
print("sumenv after eating",sumenv)

total_store = 0
for i in range(num_of_agents):
    total_store += agents[i].store
print("total_store after eating",total_store)

# check have we lost any?
if (total_store + sumenv) != sumenv0:
    print("lost some")

fdsafas = 10
for i in range(num_of_agents):
    agents[i].share(fdsafas)
    
print(agents[0])
        
#agents.append(agentframework.Agent(agents, environment, 0, 75))
#agents.append(agentframework.Agent(agents, environment, 150, 0))
#agents.append(agentframework.Agent(agents, environment, 299, 150))
#agents.append(agentframework.Agent(agents, environment, 75, 299))
'''
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
        
'''
print ("Hello World")