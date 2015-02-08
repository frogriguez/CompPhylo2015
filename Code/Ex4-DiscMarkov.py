"""
Zachary Rodriguez
CompPhylo 2015
Ex4 - Discrete Markov Chains
02/10/2015
"""

#Imports
import numpy as np
import random
#import scipy U(0,1)

"""
In this exercise, we will explore Markov chains that have discrete state spaces
and occur in discrete time steps. To set up a Markov chain, we first need to 
define the states that the chain can take over time, known as its state space.
To start, let's restrict ourselves to the case where our chain takes only two
states. Create the names of the chain's states:
"""

elements = ('A,B')
MC1 = [x+y for x in elements for y in elements]
print (MC1)
"""
Next, set up a matrix of probabilities as a list of lists
consisting of 0.2, & 0.8
"""
#mat1 = [["A",0.2,0.8],["B",0.8,0.2]]

mat1 = [[0.3,0.7],[0.4,0.6]]
print(mat1)

"""Should look like this:

       │ A    B
     ──┼─────────
     A │ 0.3  0.7 
	 B │ 0.4  0.6 
"""

print (mat1[0][1])
print (mat1[0])

"""
Now, write a function that simulates the behavior of this chain over n time
steps. To do this, you'll need to return to our earlier exercise on drawing 
values from a discrete distribution. You'll need to be able to draw a random
number between 0 and 1 (built in to scipy), then use your discrete sampling 
function to draw one of your states based on this random number.
"""

"""
This function does not follow "True" Markov Chain as it does not depend
on the previous state of the chain
"""

def sample_simple():
	num = random.random()	#draws a random float from 0->1
	if num <= 0.3:
		return"A"
	else:
		return "B"

def markov_simple(n):
	states = []
	[states.append(sample_simple()) for x in range(0,n)]
	return states

print (markov_simple(10))

"""
This function samples A or B based on 
conditional probabilities listed earlier
"""

def sample(x):
	num = random.random()
	if x == 'A':
		p = 0.3
	else:
		p = 0.4
		
	if num <= p:
		return"A"
	else:
		return "B"
	

def markov(n):
	states = ["A"]
	[states.append(sample(states[-1])) for x in range(0,n)]
	return states

print (markov(10))













