# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# This assignment is best done using jupyter notebooks. Please see the following resource for enabling jupyter notebooks on VS code: https://code.visualstudio.com/docs/python/jupyter-support 
# 
# You are welcome to use a different editor.  Uploading the notebook to google collaboratory is an option but you should leave this semester with the ability to run jupyter notebooks locally.
# 
# This homework assignment will build a model of the schelling segregation simulation.  To do this we will use list comprehensions, lambda functions, classes and class inheritance. Presumably you are familiar with list comprehensions and advanced functions from 506. References to online resources will be provided to help refresh your memory. 

# %%
#### This cell contains some of the libraries that you need to run this model. These should all be easily installed. Please contact us via slack if you have problems
import random
import matplotlib.pyplot as plt
from IPython import display
import time
get_ipython().run_line_magic('matplotlib', 'inline')
random.seed(10) # for reproducible random numbers

# %% [markdown]
# First use what we learned in lecture and lab this week to define a class called Agent using a constructor. The constructor should take 2 arguments that provide attributes called x and y for the x and y location of the objects that we create. In the cell below we have incorrect code that you will need to correct to properly define the class. There are 5 errors in the code cell below (more depending on how you count instances of the same error). 

# %%
class Agent:
    def __init__(self, xlocation, ylocation):
        self.xlocation = xlocation
        self.ylocation = ylocation

# %% [markdown]
# In the code cell below is a function for plotting the agents we create. Don't worry, you won't need to know anything about plotting. All you have to do is use your knowledge of list methods to add the x and y coordinates of the 'agent_to_be_plotted' to our lists of coordinates to plot 

# %%
def map_an_agent(self):
    agents_XCoordinate = [] # this is an empty list that will store our X-coordinates, don't change this command
    agents_YCoordinate = [] # this is an empty list that will store our y-coordinates, don't change this command
    
    #### in this line add the x attribute of the agent to be plotted to the list agents_XCoordinate. There's a built in list method - you don't need a loop
    agents_XCoordinate.append(self.xlocation)
    #### in this line add the y attribute of the agent to be plotted to the list agents_XCoordinate. There's a built in list method - you don't need a loop
    agents_YCoordinate.append(self.ylocation)
    
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('azure')
    ax.plot(agents_XCoordinate, agents_YCoordinate, 'o', markerfacecolor='purple')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created")
    plt.show()

# %% [markdown]
# In the code cell below create an instance of the class Agent and assign it to a variable called agent1. give your agent an x position of 22 and a y position of 55. then call the map_an_agent function to produce a map.  The map that gets made should look like Plot1 in the pdf that comes with this assignment.

# %%
#Initialize 1 agent.
agent1 = Agent(22,55)
###call the function from the prior cell to draw a map of where your agent is.
map_an_agent(agent1)

# %% [markdown]
# Now instantiate another object from the class Agent and assign it to a variable called agent2. give this agent an x position of 66 and a y position of 88. Again, call the map_an_agent function to produce a map.  The map that gets made should look like Plot2 in the pdf that comes with this assignment.

# %%
agent2 = Agent(66,88) 
####call the function to map this agent
map_an_agent(agent2)

# %% [markdown]
# Did you notice that we can only map 1 agent at a time with our prior function?  Let's modify our function so it will map all our agents. The way that we can do this is by passing a list of agents as the input argument for this function. Last time we directly added the attributes into the agents_XCoordinate and agents_YCoordinate list.  Let's change that command so that it adds the attributes of all the objects in a list.  There are a couple of ways to do this but for now you can use a for loop.

# %%
def map_all_agents(self):  # what arguments should go in this function?

    agents_XCoordinate = [] # this is an empty list that will store our X-coordinates, don't change this command
    agents_YCoordinate = [] # this is an empty list that will store our y-coordinates, don't change this command
    
    #Use a for loop to add all the x attributes from our list of objects to the agents_XCoordinate list and all the y attributes from our list of objects to the agents_YCoordinate list 
    for xloc in self:
        #print(xloc.xlocation)
        agents_XCoordinate.append(xloc.xlocation)
    for yloc in self:
        #print(yloc.ylocation)
        agents_YCoordinate.append(yloc.ylocation)    
        
        
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('azure')
    ax.plot(agents_XCoordinate, agents_YCoordinate, 'o', markerfacecolor='purple')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created")
    plt.show()

# %% [markdown]
# Now add the two agents we have created to a list, lets call it agents_list.  Then use the function we just created to map those agents. The map you generate should be identical to plot 3 in the pdf.

# %%
agents_list = [agent1, agent2]### add the agents we have created previously to this list
##Use the function we just created to map our agents
map_all_agents(agents_list)

# %% [markdown]
# Look at the following cell. What do you think will happen when you run it? What will happen if you run it twice? Or three times? What if I told you, it would print 73 each time you tried it. Go ahead and try it.

# %%
random.seed(10)
print(random.randint(0,100))


# %%


# %% [markdown]
# It prints 73, because thats the first random number generated with that command if we use random.seed(10). This is how we will make sure that we have the same output even though the model requires random numbers to move. Below is a function that randomly updates the attribute of each agent in our list. But I made a mistake in constructing that function. I also made a mistake in how I called the functions in that cell. If you fix those you should see a plot equivalent to Plot4 in the pdf. If you compare plot 3 and plot 4 you will see that the agents moved to their newly defined positions!

# %%
random.seed(32)
def moveagents(listofagents):
    for each_agent in listofagents:
        each_agent.xlocation = random.randint(0,100)
        each_agent.ylocation = random.randint(0,100)
moveagents(agents_list)
map_all_agents(agents_list)
map_all_agents(agents_list)


# %%


# %% [markdown]
# Now lets do something fun. lets move the agents and map them 10 times in a row. write a loop that will implement these commands. Not every command has to go inside the loop. If your agents aren't 'moving' or your final map doesn't match plot 5 in the pdf then your order is wrong. Think about the logical way to execute the loop so that the final position of the agents are mapped.

# %%
#put these commands into a loop that implement them 10 times. Not all commands have to go in the loop
#these commands are not necessarily in the right order

random.seed(66) # feed the value to random.randint
for i in range(10):
    moveagents(agents_list) #make it move
    map_all_agents(agents_list) #show it
    time.sleep(1) #keep this command 4th
    display.clear_output(wait=True) #keep this command last


# %% [markdown]
# Let's make the above loop a function that we can use on any list. Call your function make_agents_dance. What arguments should you use for this function if you want it to be generalizabe, meaning it can map any list of agents? Also make the function capable of running for any specified number of steps instead of just 10. Don't forget to make sure that the last graph stays on the screen.  

# %%
def make_agents_dance(agentlist, steps):
    for i in range(steps):
        moveagents(agentlist) #make it move
        map_all_agents(agentlist) #show it
        time.sleep(1) #keep this command 4th
        display.clear_output(wait=True) #keep this command last

#random.seed(66)
#make_agents_dance(agents_list, 15)

# %% [markdown]
# Below is an example of a list comprehension, presumably you learned this in 506. Run the cell below to remind you what a list comprehension is 
# #visit https://www.w3schools.com/python/python_lists_comprehension.asp for more information

# %%

list_made_with_listcomprehension = [i*10 for i in range(10)]
list_made_with_listcomprehension

# %% [markdown]
# Now use a list comprehension to make 12 agents within a list called New_List_of_Agents. Remember that all you need to do make an object of the class agent is provide an x and a ylocation. Lets use random.randint(0,100) to provide each of those values. Check your final output vs plot6 in the pdf

# %%
random.seed(44)  
New_List_of_Agents = [Agent(random.randint(0,100),random.randint(0,100))for i in range(12)]  ### you can model your list comprehension on the example above. you really don't need a for loop. Make 12 agents.
make_agents_dance(New_List_of_Agents, 10)

#New_List_of_Agents = []
#for i in range(12):
#    i = Agent(random.randint(0,100),random.randint(0,100))
#    New_List_of_Agents.append(i)
#print(New_List_of_Agents)
                            

# %% [markdown]
# Now lets make a subclass of Agent called AgentNew.  Agent new, in addition to its x and y coordinate attributes, should also have attributes called status and group, that will keep track of which group each instance of AgentNew is part of, and that instance is 'happy' or 'unhappy'.  Use status="unhappy" in the constructor to establish a default value of unhappy.
# 
# There are several errors in the code for defining the class below. Once you have fixed those errors, write a command to print the x, y and group of the last agent in your list. They should be, 28, 87, and purple, respectively.

# %%
class AgentNew(Agent):
    def __init__(self, x, y, group, status="unhappy"):
        #self.xlocation = x
        #self.ylocation = y
        super().__init__( x, y)
        self.group = group
        self.status = status
       
        
random.seed(23)
groups = ["Purple", "Gold"]
list_of_NewAgents = [AgentNew(random.randint(0,100), random.randint(0,100), random.choice(groups)) for x in range(35)]
print(list_of_NewAgents[-1].xlocation,list_of_NewAgents[-1].ylocation, list_of_NewAgents[-1].group)

# %% [markdown]
# the above code randomly picks whether an agent will be purple or gold.  We may want to specify that. So, lets create two subclasses of AgentNew. Let's call them PurpleAgents and GoldAgents. Below i have flawed subclass of Purple Agents created. You can fix it simply by deleting/editing the mistakes i have made. You don't have to add any new lines.
# 
# When you fix it, go ahead and create an analogous subclass called GoldAgents which has the default group="Gold"

# %%

class PurpleAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group="Purple", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)

b1 = PurpleAgents(3,6)
print(b1.group)        
        
class GoldAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group="Gold", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)    
c1 = GoldAgents(3,6)
print(c1.group)

# %% [markdown]
# Let's test out our new classes and see if they work. If you complete the code in the cell below you should get a figure that looks like plot 7 in teh pdf

# %%
random.seed(15)
List_of_PurpleAgents = [PurpleAgents(random.randint(0,100), random.randint(0,100)) for x in range(12)]  ### using list comprehension make 12 PurpleAgents
List_of_GoldAgents = [GoldAgents(random.randint(0,100), random.randint(0,100)) for x in range(12)] ### using list comprehension make 12 GoldAgents.
CombinedList = List_of_PurpleAgents+List_of_GoldAgents  #### using your knowledge of list methods, combine these into 1 list




def map_colorful_agents(c_list):  # what argument should go in this function?

    Purple_XCoordinate = [agent.xlocation for agent in c_list if agent.group=="Purple"] ####fill in the blanks to make this list comprehension work
    Purple_YCoordinate = [agent.ylocation for agent in c_list if agent.group=="Purple"] #model this after the above list comprehension
    Gold_XCoordinate = [agent.xlocation for agent in c_list if agent.group=="Gold"]
    Gold_YCoordinate = [agent.ylocation for agent in c_list if agent.group=="Gold"]
   
  
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('azure')
    ax.plot(Purple_XCoordinate, Purple_YCoordinate, 'o', markerfacecolor='purple')
    ax.plot(Gold_XCoordinate, Gold_YCoordinate, 'o', markerfacecolor='gold')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created")
    plt.show()
####call the function appropriately
map_colorful_agents(CombinedList)

'''
#print(List_of_PurpleAgents)  ### using list comprehension make 12 PurpleAgents
#print(List_of_GoldAgents ) ### using list comprehension make 12 GoldAgents.
#print(CombinedList)  #### using your knowledge of list methods, combine these into 1 list

def map_colorful_agents(c_list):
    Purple_XCoordinate = []
    for agent in c_list:
        print(agent)
        if agent.group=="Purple":
               Purple_XCoordinate.append(agent.xlocation)
    Purple_YCoordinate = []
    for agent in c_list:
        print(agent)
        if agent.group=="Purple":
               Purple_YCoordinate.append(agent.ylocation)
    Gold_XCoordinate = []
    for agent in c_list:
        print(agent)
        if agent.group=="Gold":
               Gold_XCoordinate.append(agent.xlocation)
    Gold_YCoordinate = []
    for agent in c_list:
        print(agent)
        if agent.group=="Gold":
               Gold_YCoordinate.append(agent.ylocation)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('azure')
    ax.plot(Purple_XCoordinate, Purple_YCoordinate, 'o', markerfacecolor='purple')
    ax.plot(Gold_XCoordinate, Gold_YCoordinate, 'o', markerfacecolor='gold')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created")
    plt.show()
'''

# %% [markdown]
# Now that we have some agents of different groups, lets go back and add a method to AgentNew that allows agents to move if they are unhappy. 

# %%
random.seed(38)
class AgentNew(Agent):
    def __init__(self, x, y, group, status="unhappy"):
        #self.xlocation = x
        #self.ylocation = y
        super().__init__( x, y)
        self.group = group
        self.status = status
        
######<Paste in your constructor>
    
    def move_if_unhappy(self): #what arguement(s) are needed here.
        if self.status == "unhappy":  #### there is a mistake in this command - fix it
            self.x = random.randint(0,100)
            self.y = random.randint(0,100)

a55 = AgentNew(24,11,"Purple")

a55.move_if_unhappy()  # there is something wrong with this command - fix it

print(a55.x)  ### if your class is set up right the printed answer should be 81 not 24

# %% [markdown]
# Let's take a quick timeout to cover filter and lambda functions. We'll need this when we write a method to help our agents calculate what group their neighbors are in.  A lambda function is a simple way of making a one-time use function. think of lambda q as saying for q, applied to the second argument. Filtering is applying a lambda function to a list for the purposes of filtering it.  Take a look at this next code block. What do you think is going to get printed out? If you're not sure, take a look at: https://www.w3schools.com/python/python_lambda.asp and https://www.w3schools.com/python/ref_func_filter.asp

# %%
seq = [0, 1, 2, 3, 5, 8, 13]
b = 5 
seq = list(filter(lambda q: (b-3) < q < (b + 4), seq))
print(seq)

# %% [markdown]
# Now, we're going to make our most complicated method. We're going to build a method called check_neighbors which will identify the agents that are within 10  x-coordinate spaces or 10 y-coordinate spaces of a given agent. Once those agents are  identified, we'll calculate if enough of them are of the same group to meet our pre-determined threshold. fill in the code below and see if you can do it. 

# %%
class AgentNew(Agent):
    def __init__(self, x, y, group, status="unhappy"):
        #self.xlocation = x
        #self.ylocation = y
        super().__init__( x, y)
        self.group = group
        self.status = status

    #########  PASTE in CONSTRUCTOR #########
    
    def move_if_unhappy(self): #what arguement(s) are needed here.
        if self.status == "unhappy":  #### there is a mistake in this command - fix it
            self.xlocation = random.randint(0,100)
            self.ylocation = random.randint(0,100)    
            
    ######### paste in move_if_unhappy method.

    def check_neighbors(self, agentlist):  
        # note this method needs not only the self attributes - it also needs a list of agents
        zlist = [] #this is an empty list 
        zlist = list(filter(lambda xloc : -10 < self.xlocation - xloc.xlocation < 10, agentlist)) 
        #print(zlist)
        ##### here build use a lambda function just as in the prior cell to find all agents in a list who are within 10 spaces in the X direction of the agent that is calling the method
        zlist = list(filter(lambda yloc : -10 < self.ylocation - yloc.ylocation < 10, zlist))
        ###### do the same thing now to filter for agents within 10 spaces in the y dimension. what list do you want to apply this lambda function to?
        same_group_neighbor = [agent for agent in zlist if agent.group == self.group]  
        #### use list comprehension to only keep members of zlist who are of the same group as this agent
        opposite_group_neighbor = [agent for agent in zlist if agent.group != self.group] #
        #### use list comprehension to only keep members of zlist who are of the opposite group as this agent
        #print(len(same_group_neighbor), "same group neighbors, and ", len(zlist), " total neibhors" ) ### this is commented out but you can use this as a diagnostic to make sure its working.
        if (len(same_group_neighbor)+.01)/(len(zlist)+.01) > group_affinity_threshold: #this command works. It checks the percentage of same group neighbors against some threshold to determine the agents happyness.
            self.status="happy"
        else:
            self.status="unhappy"
        
        return 
        ####### even if you successfully write in all the commands this method still won't work. something is missing. What do you think it is? Hint - refer to the farmers market mask announcement example from lecture.
        


        


# %% [markdown]
# Now that you've added some methods to the class AgentNew --- can you call them from the child class?  Why or why not?  Test below and find out. If necessary, add some code to make those method available to objects from the classes PurpleAgents and GoldAgents

# %%
class PurpleAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group="Purple", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)  
        
class GoldAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group="Gold", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status) 

random.seed(34)
p32 = PurpleAgents(14,55)
p32.move_if_unhappy()
print(p32.xlocation)  #what do you expect the output to be?

# %% [markdown]
# Now we're ready to put it all together and run a few simulations. First lets run a simulation in which there are 200 Purple and 200 Gold agents. Set the group_affinity_threshold at .51 This means that each purple or gold agent, wants to be a 'block' that is majority of their group. But as long as its a majority they will be satisfied. What happens after 15 turns?  To make sure you're running the simulation correctly test against plot 8 and plot 9 in the pdf.
# 

# %%
random.seed(2021)
group_affinity_threshold = .51
testlist = [PurpleAgents(random.randint(0,100), random.randint(0,100)) for x in range(200)] + [GoldAgents(random.randint(0,100), random.randint(0,100)) for x in range(200)] ###### create a testlist that has 200 PurpleAgents and 200 GoldAgents
map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors(testlist)  #does this need any arguments?
    for agent in (testlist):
        agent.move_if_unhappy() # does this need any arguments?
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)

# %% [markdown]
# What happens if we run it again but with a threshold of only 0.4? modify the cell below to test it out - but this time lets do it with 400 of each

# %%
random.seed(202)
group_affinity_threshold = .4 
testlist = [PurpleAgents(random.randint(0,100), random.randint(0,100)) for x in range(400)] + [GoldAgents(random.randint(0,100), random.randint(0,100)) for x in range(400)] ###### create a testlist that has 200 PurpleAgents and 200 GoldAgents
map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors(testlist)  #does this need any arguments?
    for agent in (testlist):
        agent.move_if_unhappy() # does this need any arguments?
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)

# %% [markdown]
# Even if people don't mind being a minority in their neighborhood - you still get segregation pretty easily according to this model. For a long time models such as this were used to argue that some degree of segregation was inevitable, and therefore it should not be a target of policy. 
# 
# Let's challenge that assumption. Make 2 new subclasses, PurpleDiveristySeekers and GoldDiversitySeekers. Please use those exact names to allow for autograding. And for these subclasses make them seek out diversity instead of avoid it. Run some simulations with 300 traditional Purple and Gold Agents and 100 Purple and GOld Diversity Seeker agents each.  What happens then? Use random.seed(11) in each of the remaining cells.

# %%
### Use this and additional cells to run the additional simulation.

# %% [markdown]
# Additional information. 
#  - please do the recommended reading on Classes & inheritance in Head First Python
#  - to read the original Schelling Paper: https://www.uu.nl/sites/default/files/c4_schelling1969_models_segregation.pdf (this is not required at all)
#  - for a thoughtful discussion about what we can learn from models such as these, check out: https://www.e-flux.com/architecture/representation/159207/the-simple-societies-of-complex-models/ 

# %%



